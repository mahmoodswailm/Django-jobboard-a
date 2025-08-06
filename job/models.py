from django.db import models
from django.utils.text import slugify 
from django.contrib.auth.models import User
#helper function to get the upload path
def Upload(instance,image:str):
    # image_name,extension = image.split(".")
    extension = image.split(".")[1]
    return f"job/{instance.id}.{extension}"
    # return "job/%s.%s" %(instance.id,extension)
    
# Create your models here.
class Job(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name="job_user")
    title = models.CharField(max_length=100)
    # location = models
    jobtype = models.CharField(max_length=15,
                            choices=[
                                ("FullTime","FullTime"),
                                ("PartTime","PartTime")
                            ])
    # Publisher = models.CharField( max_length=50)
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    Vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0,verbose_name="salary in (USD)")
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    experience = models.IntegerField(default=0,verbose_name="Year")
    image = models.ImageField( upload_to= Upload )
    slug =  models.SlugField(max_length=40,
                            # unique=True,
                            null=True,
                            blank=True)  
    
    def save(self,*args,**kwargs):
        # if not self.slug:
        self.slug = self.title.replace(" ","-").lower()
        # self.slug = slugify(self.title) # means modify slug after save
        super(Job,self).save(*args,**kwargs) # and let save method does what it does  
        
    
    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=25)
    
    def __str__(self):
        return self.title


class Apply(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    website = models.URLField(max_length=100,blank=True,null=True)
    cv = models.FileField(upload_to='cv/',null=True,blank=True)
    coverletter = models.TextField(max_length=500,blank=True,null=True)
    
    job = models.ForeignKey(Job, related_name="apply_job",on_delete=models.CASCADE)
        # related_name sets the name for the reverse relation from Job to Apply.
        # It makes it easy to get all applications for a specific job.
        # job = Job.objects.get(id=1)
        # applications = job.apply_job.all()  # Gets all Apply objects for this job
        
    applied_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
        # return f"{self.name} applied for {self.job.title}"