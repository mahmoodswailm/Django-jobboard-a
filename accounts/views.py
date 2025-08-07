from django.shortcuts import render
from . import models
from .forms import SignUpForm
from django.contrib.auth import authenticate,login
from django.shortcuts import redirect
# Create your views here.

def sign_up(request):
    if request.method == "method":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username= form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect("/accounts/registration/Profile")
    else:
        form = SignUpForm()
    
    return render(request, "registration/sign_up.html", {"form": form})


def Profile(request):
    if request.user.is_authenticated:
        user = request.user
        return render(request, "registration/Profile.html", {"user": user})
    else:
        return redirect("/accounts/login/")



def Login(request):
    if request.user.is_authenticated:
        return redirect("/accounts/registration/Profile/")
    else:
        return render(request, "registration/login.html")