from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse

# Create your models here.
class UserProfile(models.Model):
    bio=models.CharField(max_length=100)
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    picture=models.ImageField(upload_to="profile_picture",default='user.png')

    def get_absolute_url(self):
        return reverse("profile", kwargs={"pk": self.pk})
    
    
class Education(models.Model):
    school = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    field = models.CharField(max_length=100)
    start=models.DateTimeField()
    end=models.DateTimeField(null=True)
    description = models.TextField()
    
class Experience(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    start=models.DateTimeField()
    end=models.DateTimeField(null=True)
    description = models.TextField()

@receiver(post_save,sender=User)
def createUserProfile(sender,instance,**kwargs):
    if UserProfile.objects.filter(user=instance).count()==0:
        UserProfile.objects.create(user=instance)