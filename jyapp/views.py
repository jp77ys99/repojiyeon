from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request) :
    return render(request, 'home.html')

def homestring(request, jiyeon) :
    return render(request, 'homestring.html', {'jieun':jiyeon})