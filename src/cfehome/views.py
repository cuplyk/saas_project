from django.http import HttpResponse
from django.shortcuts import render
from visits.models import PageVisit
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
import pathlib

from django.conf import settings

LOGIN_URL = settings.LOGIN_URL

this_dir = pathlib.Path(__file__).resolve().parent

def home_views(request, *args, **kwargs):
    """
    This function handles the home page view.
    It returns a simple HTML response with a welcome message.
    """
    return about_views(request, *args, **kwargs)


def about_views(request, *args, **kwargs):
    """
    This function handles the home page view.
    It returns a simple HTML response with a welcome message.
    """
    if request.user.is_authenticated:
        print(request.user.first_name)
        
    
    qs = PageVisit.objects.all()
    page_qs = PageVisit.objects.filter(path=request.path)
    try:
        percent = (page_qs.count() * 100.0) / qs.count()
    except:
        percent = 0
    my_title = "My Page"
    html_template = "home.html"
    my_context = {
        "page_title": my_title,
        "page_visit_count": page_qs.count(),
        "percent": percent,
        "total_visit_count": qs.count(),
    }
    PageVisit.objects.create(path=request.path)
    return render(request, html_template, my_context)

def index_views(request, *args, **kwargs):
    """
    This function handles the index page view.
    It returns a simple HTML response with a welcome message.
    """
    my_title = "My Page"
    my_context = {
        "page_title": my_title,

    }
    return render(request, "index.html", my_context)

VALID_CODE = "aaa1234"

def pw_protected_view(request, *args, **kwargs):
    is_allowed = request.session.get('protected_page_allowed', 0)
    #print(request.session.get('protected_page_allowed'), type(request.session.get('protected_page_allowed')))
    if request.method == "POST":
        user_pw_sent = request.POST.get("code") or None
        if user_pw_sent == VALID_CODE:
            is_allowed = 1
            request.session['protected_page_allowed'] = is_allowed
    if is_allowed:
        return render(request, "protected/view.html", {})
    return render(request, "protected/entry.html", {})

@login_required(login_url=LOGIN_URL)
def user_only_view(request, *args, **kwargs):
    print(request.user.is_staff)
    return render(request, "protected/user_only.html", {})

@staff_member_required(login_url=LOGIN_URL)
def staf_only_view(request, *args, **kwargs):
    return render(request, "protected/user_only.html", {})