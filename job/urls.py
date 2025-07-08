# this file is created to refere to logic that render data to frontend

from django.urls import path
from .views import job_details,job_list

# adding paths of logic
urlpatterns = [
    path('',job_list),
    path('<int:id>',job_details) # show jobdetail by id which here is integer
]