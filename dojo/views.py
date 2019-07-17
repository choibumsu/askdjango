from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def mysum(request, numbers):
    return HttpResponse(sum(map(int,numbers.split('/'))))