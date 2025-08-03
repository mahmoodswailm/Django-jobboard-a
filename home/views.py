from django.shortcuts import render
from job.models import Job 
# Create your views here.
def Home(request):
    # return render
    context ={"jobs":Job.objects.all()}
    return render(request,"home/index.html",context)