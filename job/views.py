from django.shortcuts import render
from .models import Job    
# Create your views here.

def job_list(request):
    jobs =Job.objects.all
    return render(request,"job\jobs.html", context={
        "jobs":jobs
    })

def job_details(request,id):
    job = Job.objects.get(id=id)
    return render(request,
                "job\job_details.html",
                context={
        "job_de":job
    })