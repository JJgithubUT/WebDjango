from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home/index.html')

def contact(request):
    return render(request, 'home/contact.html')

def projects(request):
    return render(request, 'home/projects.html')

def about(request):
    return render(request, 'home/about.html')