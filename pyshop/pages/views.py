from django.http import  HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request,*args,**kwargs):
    return render(request,'home_view.html',{ })

def contact_view(request,*args,**kwargs):
    return render(request,'contact.html',{})

def about_view(*args,**kwargs):
    return HttpResponse("<h1>about page</h1>")
