from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def address(request):
    return render(request,'address.html')
def info(request):
    return render(request,'info.html')
