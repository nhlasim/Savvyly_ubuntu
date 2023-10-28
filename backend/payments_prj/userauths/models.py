from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser): #abstract user allos us to overried the current use model to use email as login name
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)    #use 'Emailfield' so django can make some email validations for us
    is_staff = models.BooleanField(default=False)  #reason we are adding 'is_staff  because we are going to create a custom form that will help us create superusers from site
    is_superuser = models.BooleanField(default=False) 
    
    USERNAME_FIELD = 'email' #looks like a system field that is already built into django
    REQUIRED_FIELDS = ['username'] #looks like a system field that is already built into django
    
    def __str__(self):   #create a string representation 
        return self.username

#user.is_staff = True