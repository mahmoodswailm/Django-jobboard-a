from django.contrib import admin
from .models import Profile, City
# Register your models here.

admin.site.register(Profile)  # Show Profile model in admin site
admin.site.register(City)  # Show City model in admin site