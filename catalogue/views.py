from django.shortcuts import render

# Create your views here.

def home_page(request):
    return render(request, 'index.html')

def catalogue_page(request):
    return render(request, 'catalogue.html')

def cap_page(request):
    return render(request, "cap.html")

def ironman_page(request):
    return render(request, "ironman.html")