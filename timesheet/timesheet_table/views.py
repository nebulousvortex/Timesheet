from operator import attrgetter

from django.contrib.auth import logout, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
import datetime
import calendar

from .forms import RegisterUserForm, LoginUserForm
from .models import Timesheet
from .utils import DataMixin

rus_weekdays = {
    1: 'Понедельник',
    2: 'Вторник',
    3: 'Среда',
    4: 'Четверг',
    5: 'Пятница',
    6: 'Суббота',
    7: 'Воскресенье'
}


class TimeSheetView(LoginRequiredMixin, ListView):
    model = Timesheet
    template_name = 'timesheet_table/home.html'
    context_object_name = 'timesheet'
    login_url = reverse_lazy('not_auth')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Расписание'

        timesheet = context['timesheet']

        grouped_timesheet = {}
        timesheet_sorted_by_week = sorted(timesheet, key=attrgetter('week_id', 'day_id', 'time'))

        for elem in timesheet_sorted_by_week:
            week = elem.week
            day = elem.day
            if week not in grouped_timesheet:
                grouped_timesheet[week] = {}
            if day not in grouped_timesheet[week]:
                grouped_timesheet[week][day] = []
            grouped_timesheet[week][day].append(elem)

        context['grouped_timesheet'] = grouped_timesheet

        context['current_class'], context['next_class'] = self.get_classes(grouped_timesheet)

        return context

    def get_classes(self, grouped_timesheet):
        current_week = self.get_current_week('28.08.2023')
        current_day = rus_weekdays[self.get_current_day()]
        current_time = datetime.datetime.now().time()
        found_current_entry = False
        found_next_entry = False
        for week, week_days in grouped_timesheet.items():
            if str(week).strip() == str(current_week).strip():
                for day, entries in week_days.items():
                    if str(day).strip() == str(current_day).strip():
                        print(entries)
                        for entry in entries:
                            print(entry.time >= (datetime.datetime.now() - datetime.timedelta(hours=1, minutes=30)).time())
                            print(entry.time, ' - ',(datetime.datetime.now() - datetime.timedelta(hours=1, minutes=30)).time())
                            if current_time >= entry.time and entry.time >= (datetime.datetime.now() - datetime.timedelta(hours=1, minutes=30)).time():
                                current_class = entry
                                found_current_entry = True
                            elif current_time < entry.time:
                                next_class = entry
                                found_next_entry = True
                                break

                            print(f"Week: {week}, Day: {day}, Entry: {entry.time}")

        current_class_entity = ""
        next_class_entity = ""

        if found_current_entry:
            current_class_entity = current_class

        if found_next_entry:
            next_class_entity = next_class

        return current_class_entity, next_class_entity

    def get_current_day(self):
        current_date = datetime.datetime.now().date()
        return current_date.isocalendar()[2]

    def get_current_week(self, start_date):
        start_week = datetime.datetime.strptime(start_date, "%d.%m.%Y").date().isocalendar()[1]
        current_week = datetime.datetime.now().date().isocalendar()[1]
        weeks_passed = current_week - start_week
        if weeks_passed % 2 == 0:
            return "Числитель"
        else:
            return "Знаменатель"


def not_auth(request):
    return render(request, 'timesheet_table/not_auth.html')


def logout_user(request):
    logout(request)
    return redirect('login')


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = "timesheet_table/register.html"
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = "timesheet_table/login.html"

    def get_success_url(self):
        return reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Авторизация')
        return dict(list(context.items()) + list(c_def.items()))
