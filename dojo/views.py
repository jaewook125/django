# dojo/views.py
from django.http import HttpResponse
from django.shortcuts import render

def mysum(request, numbers):
    # request: HttpResponse
    # numbers = "1/2/123/123/132/1215/123123"
    result = sum(map(lambda s: int(s or 0), numbers.split("/")))
    return HttpResponse(result)

# Create your views here.
