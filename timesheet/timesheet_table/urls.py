from django.contrib import admin
from django.urls import path

from . import views
from .views import TimeSheetView

urlpatterns = [
    path('', TimeSheetView.as_view(), name="home"),
    path('logout/', views.logout_user, name="logout"),
    path('login/', views.LoginUser.as_view(), name="login"),
    path('register/', views.RegisterUser.as_view(), name="register"),
    path('not_login_user/', views.not_auth, name="not_auth"),
]