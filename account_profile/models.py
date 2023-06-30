from django.db import models

from django.contrib.auth.models import User

# Create your models here.
# profile

class account_profile(models.Model):
    #key
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    

    #field
    flavor_bio = models.TextField(null=True, blank= True)
    avatar_url = models.CharField(max_length=1000, default='/imgs/default_avatar.png')
    website_url = models.CharField(max_length=1000, null=True, blank= True)
    created_at = models.DateTimeField(auto_now_add=True, )
    updated_at = models.DateTimeField(auto_now=True,)
    dob = models.DateField(null=True, blank= True)
    gender = models.SmallIntegerField(null=True, blank= True)
    address = models.CharField(max_length=200 , null = True, blank = True)
    city = models.CharField(max_length=50, null=True, blank= True)
    country = models.CharField(max_length=50, null=True, blank= True)
    