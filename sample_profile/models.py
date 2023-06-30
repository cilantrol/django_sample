import datetime
from django.db import models

from django.contrib.auth.models import User

# Create your models here.
# profile

class Profile(models.Model):
    #enum
    GENDER_CHOICES = (
        (1, 'Male'),
        (2, 'Female'),
        (3, 'Other'),
        (4, 'Prefer not to say'),
    )
    
     
    #key
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    # user_id = models.IntegerField(null=False)
    # was previously user, did not work, django requires the field to be user_id
    # want to maintain one to one relationship with user
    
    #field
    flavor_bio = models.TextField(null=True, blank= True)

    created_at = models.DateTimeField(auto_now_add=True, )
    updated_at = models.DateTimeField(auto_now=True,)
    dob = models.DateField(null=True, blank=True)
    gender = models.SmallIntegerField(choices=GENDER_CHOICES, null=True, blank= True)
    address = models.CharField(max_length=200 , null = True, blank = True)
    city = models.CharField(max_length=50, null=True, blank= True)
    country = models.CharField(max_length=50, null=True, blank= True)
    # avatar_url = models.CharField(max_length=1000, default='/imgs/default_avatar.png', null=True, blank= True)
    # website_url = models.CharField(max_length=1000, null=True, blank= True)
    



