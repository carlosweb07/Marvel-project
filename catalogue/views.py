from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

def home_page(request):
    return render(request, 'index.html')

@login_required
def catalogue_page(request):
    return render(request, 'catalogue.html')

@login_required
def cap_page(request):
    return render(request, "cap.html")

@login_required
def ironman_page(request):
    return render(request, "ironman.html")

@login_required
def spiderman_page(request):
    return render(request, "spider.html")

@login_required
def thor_page(request):
    return render(request, "thor.html")