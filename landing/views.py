from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "landing/index.html")

def about(request):
    return render(request, "landing/about.html")

def contact(request):
    return render(request, "landing/contact.html")

def projects(request):
    return render(request, "landing/projects.html")