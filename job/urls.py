# this file is created to refere to logic that render data to frontend

from django.urls import path
from .views import job_details,job_list

# this file is created to refere to logic that render data to frontend
# this file is used to define the urls for the job app

app_name = "job"  # this is used to refer to the app in the templates


# adding paths of logic
urlpatterns = [
    path('',job_list,name="job_list"),  # show all jobs
    # path('<int:id>',job_details,name="job_details") # show jobdetail by id which here is integer
    path('<str:slug>/',job_details,name="job_details") # show jobdetail by id which here is integer
]