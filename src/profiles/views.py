from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from django.contrib.auth import get_user_model

User = get_user_model()




@login_required
def profile_list_views(request, *args, **kwargs):

    context = {
        "object_list": User.objects.filter(is_active=True)
    }
    return render(request, "profiles/list.html", context)




@login_required
def profile_detail_view(request, username=None, *args, **kwargs):
    """
    This function handles the profile page view.
    """
    user = request.user
    
    my_title = "Profile Page"
    my_context = {
        "page_title": my_title,
    }
    #profile_user_obj = User.objects.get(username=username)
    profile_user_obj = get_object_or_404(User, username=username)
    is_me = profile_user_obj == user
    context = {
        "object": profile_user_obj,
        "instance": profile_user_obj,
        "owner": is_me,
    }
    return render(request, "profiles/detail.html", context)