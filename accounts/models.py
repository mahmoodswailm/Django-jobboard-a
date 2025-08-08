from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    bio = models.TextField(blank=True, null=True) #biography 
    city = models.ForeignKey('City',on_delete=models.CASCADE,max_length=100,blank=True,null=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.username


class City(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    country = models.CharField(max_length=100,blank=True,null=True)
    state = models.CharField(max_length=100,blank=True,null=True)
    name = models.CharField(max_length=100,blank=True,null=True)

    def __str__(self):
        return f"{self.name}, {self.state}, {self.country}"
    

from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_profiel_receiver(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

