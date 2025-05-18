from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
# Create your views here.

def login_view(request, *args, **kwargs):
    """
    This function handles the login page view.

    """
    username = "root2"#request.POST.get("username")
    password = "djangoadmin"#request.POST.get("password")
    # Check if the user has the correct credentials
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        print("log in here")
        return redirect("/")
    return render(request, "auth/login.html", {})


