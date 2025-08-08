from django.shortcuts import render
from .models import *
from .forms import *
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


def profile(request):
    prof= Profile.objects.get(user=request.user)
    if request.user.is_authenticated:
        user = request.user
        return render(request, "accounts/Profile.html", {"user": user,"prof": prof})
    else:
        return redirect("/accounts/login/")


def edit_profile(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == "POST":
        profileform = ProfileEditForm(request.POST, request.FILES, instance=profile)
        userform = UserForm(request.POST, instance=request.user)
        if profileform.is_valid() and userform.is_valid():
            userform.save()
            myprofile =profileform.save(commit=False)
            myprofile.user = request.user
            myprofile.save()
            return redirect("/accounts/Profile/")
    else:
        profileform = ProfileEditForm( instance=request.user.profile)
        userform = UserForm( instance=request.user)
    return render(request, "accounts/ProfileEdit.html", context={"userform":userform,"proform": profileform})





def Login(request):
    if request.user.is_authenticated:
        return redirect("/accounts/registration/Profile/")
    else:
        return render(request, "registration/login.html")