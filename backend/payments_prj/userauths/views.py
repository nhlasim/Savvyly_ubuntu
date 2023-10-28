from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from userauths.models import User
from userauths.forms import UserRegisterForm

def RegisterView(request): #function based view where we say what our api will do
    if request.method == "POST": #post api. forms uses specific tokenisation. we would have to implement our on example from "jwt"
        form = UserRegisterForm(request.POST)
        if form.is_valid(): #is valid is not specific to forms can be used with serialiser as well
            #form.save()
            new_user = form.save() #save the data to the database
            username = form.cleaned_data.get("username") #superfluous for api (when not using forms)
            messages.success(request, f"Hey{username}, your account was created successfully.")
            new_user = authenticate(username=form.cleaned_data['email'], 
                                    password=form.cleaned_data['password1']) #django functionality to check if someone is authenticated.
            login(request, new_user) #login the person
            return redirect("account:account")
        
    if request.user.is_authenticated: #django function to check if user is authenticated
        messages.warning(request, f"You are aready logged in")
        return redirect("account:account")
    
    else:
        form = UserRegisterForm()     
    context = {
        "form": form
    }
    return render(request, "userauths/sign-up.html", context)

def LoginView(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        try:
            user = User.objects.get(email=email)
            user = authenticate(request, email=email, password=password)

            if user is not None: # if there is a user
                login(request, user)
                messages.success(request, "You are logged in.")
                # return redirect("account:account")
                return redirect("account:dashboard") #I put this in over above
            else:
                messages.warning(request, "Username or password does not exist")
                return redirect("userauths:sign-in") #this is redicted to sign-in page but you can also redirect to sign-up page
        except:
            messages.warning(request, "User does not exist")
    
    if request.user.is_authenticated:
        messages.warning(request, "You are already logged In")
        # return redirect("account:account")
        return redirect("account:dashboard") #I put this in over above
    
    return render(request, "userauths/sign-in.html")
    
def logoutView(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect("userauths:sign-in")




    
