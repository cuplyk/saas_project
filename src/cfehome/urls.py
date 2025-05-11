# -*- coding: utf-8 -*-
from django.contrib import admin
from django.urls import path
from .views import home_views, about_views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("about/", about_views),
    path("", home_views)
]