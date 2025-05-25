# -*- coding: utf-8 -*-
from django.contrib import admin
from django.urls import path, include


from accounts.views import login_view, register_view

urlpatterns = [
    path("", home_views, name="home"),

]