# -*- coding: utf-8 -*-
from django.contrib import admin
from django.urls import path
from .views import home_views, about_views
from accounts.views import login_view, register_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("login/", login_view),
    path("register/", register_view),
    path("about/", about_views),
    path("", home_views)
]