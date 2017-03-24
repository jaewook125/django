# dojo/views.py
from django.http import HttpResponse
from django.shortcuts import render

def mysum(request, x, y=0 ,z=0):
    # request: HttpResponse
    return HttpResponse(int(x) + int(y)+ int(z))

# Create your views here.
