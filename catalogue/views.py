from django.shortcuts import render

# Create your views here.

def home_page(request):
    return render(request, 'index.html')

def catalogue_page(request):
    return render(request, 'catalogue.html')