from django.http import HttpResponse
from django.shortcuts import render
from visits.models import PageVisit
import pathlib


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