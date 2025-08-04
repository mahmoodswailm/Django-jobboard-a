from django.db import models
from django.utils.text import slugify 

#helper function to get the upload path
def Upload(instance,image:str):
    # image_name,extension = image.split(".")
    extension = image.split(".")[1]
    return f"job/{instance.id}.{extension}"
    # return "job/%s.%s" %(instance.id,extension)
    
# Create your models here.
class Job(models.Model):
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