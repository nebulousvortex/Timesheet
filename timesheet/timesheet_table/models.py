from django.db import models


class ClassType(models.Model):
    name = models.TextField("Тип пары", null=False)

    def __str__(self):
        return self.name


class Days(models.Model):
    name = models.TextField("День недели", null=False)

    def __str__(self):
        return self.name


class WeekType(models.Model):
    name = models.TextField("Тип недели", null=False)

    def __str__(self):
        return self.name


class Timesheet(models.Model):
    week = models.ForeignKey('WeekType', on_delete=models.PROTECT, null=True)
    day = models.ForeignKey('Days', on_delete=models.PROTECT, null=True)
    time = models.TimeField("Время", null=False)
    name = models.TextField("Название", null=False)
    room = models.TextField("Аудитория", null=False)
    teacher = models.TextField("Преподаватель", null=False)
    type = models.ForeignKey('ClassType', on_delete=models.PROTECT, null=True)
