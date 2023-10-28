from django import forms
from django.contrib.auth.forms import UserCreationForm #this UserCreationForm has a lot of already prebuilt fields which is why we are using
from userauths.models import User

class UserRegisterForm(UserCreationForm):
    
    class Meta: #create meta because we want to pass the "model" (User) that we are going to be interacting with, and also pass "fields" to tell the class what fields from "UserCreationForm" we want to pass/show the client
        model = User
        fields = ['username', 'email', 'password1', 'password2']