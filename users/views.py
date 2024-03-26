from django.shortcuts import render, redirect

from .crud import create_user

def login_page(request):
    return render(request, 'login.html')

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