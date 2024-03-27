from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User

from .crud import create_user

def login_page(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        user = authenticate(
            request, 
            username=request.POST["username"], 
            password= request.POST["password"],
        )
        if not user:
            return render(request, 'login.html', {
                "error": "username or password is incorrect"
            })
        login(request, user)
        return redirect("/catalogue/")

def register_page(request):
    if request.method == "GET":
        return render(request, 'register.html')
    else:
        user_data = {
            "name": request.POST["name"],
            "email": request.POST["email"],
            "password": request.POST["password"],
        }
        response = create_user(user_data)
        if(response["error"]):
            return render(request, 'register.html', {
                "error": response["msg"]
            })
        else: return redirect("/login/")