from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def fnuser(request):
    return HttpResponse("rahil are you fine")
def fnuser1(request):
    return render(request,'user1.html')    
def fnhome(request):
    return render(request,'home.html')
def fnprod(request):
    return render(request,'prod.html')     
def fnFboot(request):
    return render(request,'Fboot.html') 
def fnLboot(request):
    return render(request,'Lboot.html')    
def fnNTboot2(request):
    return render(request,'NTboot2.html')     
def fnnew(request):
    return render(request,'new.html')  
def fnmod(request):
    return render(request,'modjum.html')   
def fngridb(request):
    return render(request,'gridb.html')
def fnwb(request):
    return render(request,'wb.html')
def fnjava1(request):
    return render(request,'java1.html') 
def fnpromcon(request):
    return render(request,'promcon.html')  
def fnarith(request):
    return render(request,'arith.html')   
def fngrade(request):
    return render(request,'grade.html')  
def fnswitch1(request):
    return render(request,'switch1.html')  
def fnfibi(request):
    return render(request,'fibinocci.html')
def fnques(request):
    return render(request,'ques.html')  
def fnwhile(request):
    return render(request,'while.html') 
def fnhw(request):
    return render(request,'hw.html')     
def fncyber(request):
    return render(request,'cyber.html')                                     