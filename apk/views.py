from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def fnuser(request):
    return HttpResponse("rahil are you fine")
def fnuser1(request):
    return render(request,'user1.html')    
def fnhome(request):
    return render(request,'home.html')