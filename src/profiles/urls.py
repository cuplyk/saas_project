# -*- coding: utf-8 -*-
from django.contrib import admin
from django.urls import path, include
from . import views


from accounts.views import login_view, register_view

urlpatterns = [
    path("<username>/", views.profile_view, name="profile"),

]