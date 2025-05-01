from django.http import HttpResponse
from django.shortcuts import render
def home_page_views(request, *args, **kwargs):
    """
    This function handles the home page view.
    It returns a simple HTML response with a welcome message.
    """
    my_context = {
        "page_title": "Hello World",
    }

    html_template = "home.html"
    return render(request, html_template, my_context)