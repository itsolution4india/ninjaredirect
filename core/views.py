from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse
from .models import GotBaited , NormalVisit

def home(request): 
    
    return render(request, 'home.html' , context={'visitor' :  request.visitor})

def index(request):
    return render(request, 'index.html')
def create(request):
    return render(request, 'create.html')

def about(request):
    return render(request, 'about.html')

def foodie(request):
    return render(request, 'fodie.html')

def gotbaited(request ,  id):
    visitor  = get_object_or_404(NormalVisit , id = id )
    new_baited = GotBaited(have_clicked = True , visitor = visitor)
    new_baited.save()
    
    # print(new_baited)
  
    return None
