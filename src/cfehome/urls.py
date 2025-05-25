# -*- coding: utf-8 -*-
from django.contrib import admin
from django.urls import path, include
from .views import (
    home_views, 
    about_views, 
    pw_protected_view,
    user_only_view,
    staf_only_view
)

from accounts.views import login_view, register_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("login/", login_view),
    path("register/", register_view),
    path("about/", about_views),
    path("", home_views, name="home"),
    path("protected/", pw_protected_view),
    path("protected/user-only", user_only_view),
    path("protected/staf-only", staf_only_view),

    path('accounts/', include('allauth.urls')),
]