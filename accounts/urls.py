from django.urls import path,include
# Adding static and media URl patterns
import django.contrib.auth.urls
from .views import *

app_name = "accounts"

urlpatterns = [
    path('login/', Login, name='login'),
    # path('login/', LoginView.as_view(), name='login'),
    path('Profile/', profile, name='Profile'),
    path('ProfileEdit/', edit_profile, name='ProfileEdit'),
    path("sign_up/",sign_up,name="sign_up")
]
