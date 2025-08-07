from django.urls import path,include
# Adding static and media URl patterns
import django.contrib.auth.urls
from .views import *

app_name = "accounts"

urlpatterns = [
    # path('', include('django.contrib.auth.urls')),  # Default auth URLs
    path('login/', Login, name='login'),
    # path('login/', LoginView.as_view(), name='login'),
    path('Profile/', Profile, name='Profile'),
    # path('Profile/edit/', ProfileEdit, name='ProfileEdit'),
    path("sign_up/",sign_up,name="sign_up")
]
