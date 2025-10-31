from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def index(request):
    return render(request, 'index.html')
def create(request):
    return render(request, 'create.html')

def about(request):
    return render(request, 'about.html')

def foodie(request):
    return render(request, 'fodie.html')
