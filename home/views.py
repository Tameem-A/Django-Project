from django.shortcuts import render,HttpResponse
#from datetime import datetime
from home.models import Contact
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    #return HttpResponse('this is aboutpage')
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')

def contact(request):
    if request.method =='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        contact=Contact(email=email,password=password)
        contact.save()
        messages.success(request, 'Profile details updated.')
    return render(request,'cont.html')