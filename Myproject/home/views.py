# views.py

from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse("hello this is home page")

def about(request):
    return HttpResponse("this is about page")
