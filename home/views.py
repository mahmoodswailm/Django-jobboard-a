from django.shortcuts import render

# Create your views here.
def Home(request):
    # return render
    return render(request,"home/index.html",context={})