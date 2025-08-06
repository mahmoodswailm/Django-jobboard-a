from django.shortcuts import render
from .models import Job    
from django.core.paginator import Paginator
from django.utils.text import slugify  
from django.shortcuts import get_object_or_404
from .forms import Form, PostJob
# Create your views here.

def job_list(request):
    jobs =Job.objects.all()
    p = Paginator(jobs,1)  # Show 1 jobs per page (pagination object)
    page_num= request.GET.get("page")
    page_obj = p.get_page(page_num) 
    # page_obj is the current page of jobs
    return render(request,"job\jobs.html", context={
        "page_obj":page_obj,"jobs":jobs
    })

def job_details(request,slug):#id
    # job = Job.objects.get(id=id)
    # job = get_object_or_404(Job, title=title)
    job = Job.objects.get(slug=slug)
    if request.method =="POST":
        form = Form(request.POST,request.FILES)
        if form.is_valid():
            apply = form.save(commit=False)  # Don't save to DB yet
            apply.job =job 
            apply.save()
            # return redirect('job:job_list')  # Redirect to job list after saving
        
    
    else:
        form = Form()
    
    return render(request,
                "job\job_details.html",
                context={
        "job_de":job,"form":form
    }
    )
    
    

def Add(request):
    if request.method =="POST":
        Post = PostJob(request.POST,request.FILES)
        if Post.is_valid():
            form= Post.save(commit=False)
            form.user = request.user
            form.save()
            
    else:
        Post = PostJob()
        

    return render(request,"job\Post.html",context={"form":Post})
    
    
# Example usage of Paginator
    
# p.count
# 4
# >>> p.num_pages
# 2
# >>> type(p.page_range)
# <class 'range_iterator'>
# >>> p.page_range
# range(1, 3)

# >>> page1 = p.page(1)
# >>> page1
# <Page 1 of 2>
# >>> page1.object_list
# ['john', 'paul']

# >>> page2 = p.page(2)
# >>> page2.object_list
# ['george', 'ringo']
# >>> page2.has_next()
# False
# >>> page2.has_previous()
# True
# >>> page2.has_other_pages()
# True
# >>> page2.next_page_number()
# Traceback (most recent call last):
# ...
# EmptyPage: That page contains no results
# >>> page2.previous_page_number()
# 1
# >>> page2.start_index()  # The 1-based index of the first item on this page
# 3
# >>> page2.end_index()  # The 1-based index of the last item on this page
# 4
