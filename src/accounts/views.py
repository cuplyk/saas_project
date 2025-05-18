from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
# Create your views here.
from django.contrib.auth import get_user_model


User = get_user_model()


def login_view(request, *args, **kwargs):
    """
    This function handles the login page view.

    """
    my_title = "Login Page"
    my_context = {
        "page_title": my_title,
    }

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
    return render(request, "auth/login.html", my_context)


def register_view(request, *args, **kwargs):
    """
    This function handles the register page view.

    """
    my_title = "Register Page"
    my_context = {
        "page_title": my_title,
    }
    if request.method == "POST":
        #print(request.POST)
        username = request.POST.get("username") or None 
        email = request.POST.get("email") or None
        password = request.POST.get("password") or None

        #username_exist = User.objects.filter(username__iexact=username).exists()
        #email_exist = User.objects.filter(email__iexact=email).exists()
        try:
            User.objects.create_user(
                username=username,
                email=email,
                password=password
            )
        except:
            pass


    return render(request, "auth/register.html", my_context)