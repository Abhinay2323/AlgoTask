from django.contrib import admin
from django.urls import path, include
from userform import views

urlpatterns = [
    path('', views.home, name="home"),
    path('user-form/', views.formuser, name="userform"),
]