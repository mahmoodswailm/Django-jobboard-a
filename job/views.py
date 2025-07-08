from django.shortcuts import render
from .models import Job    
# Create your views here.

def job_list(request):
    jobs =Job.objects.all
    return render(request,"job\joblist.html", context={
        "jobs":jobs
    })
def job_details(request,id):
    job = Job.objects.get(id=id)
    return render(request,"job\jobdetail.html",context={
        "job_de":job
    })