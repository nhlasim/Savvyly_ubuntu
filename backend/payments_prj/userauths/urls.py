from django.urls import path
from userauths import views

app_name = "userauths"

urlpatterns = [
    path("sign-up/", views.RegisterView, name="sign-up"), #first path of "path" is the end point, second past is the "function" or what the api will do whether post or get
    path("sign-in/", views.LoginView, name="sign-in"),
    path("sign-out/", views.logoutView, name="sign-out"),
]
