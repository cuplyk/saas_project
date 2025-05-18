from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
# Create your views here.

def login_view(request, *args, **kwargs):
    """
    This function handles the login page view.

    """

    if request.method == "POST":
        username = request.POST.get("username") or None 
        password = request.POST.get("password") or None
        # Check if the user has the correct credentials
        if all([username, password]):
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                print("log in here")
                return redirect("/")
    return render(request, "auth/login.html", {})


