from django.contrib import admin
from . models import Job,Category
# Register your models here.

admin.site.register(Job) # SHOW  JOb model in adming site
admin.site.register(Category) # show Category in admin site
