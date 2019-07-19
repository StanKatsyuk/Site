from django.shortcuts import render
from django.http import HttpResponse
from projects.models import Project

# Create your views here.

def index(request):
    #return render(request, 'landing_page.html', {})
    context = {"home_page": "active"} 
    return render(request, 'pages/index.html', context)

def about(request):
    context = {"about_page": "active"} 
    return render(request, 'pages/about.html', context)

def projects(request):
    context = {"projects_page": "active"}
    return render(request, 'projects/project_detail.html', context)

def contact(request):
    context = {"contact_page": "active"}
    return render(request, 'pages/contact.html', context)
