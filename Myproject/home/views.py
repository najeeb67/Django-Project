# views.py

from django.shortcuts import render, HttpResponse

def index(request):
    context = {
        'title': 'first try',
        'name':"najeeb",
        'class':'django',
    }
    return render(request, "index.html" , context)
    # return HttpResponse("hello this is home page")

def about(request):
    return HttpResponse("this is about page")

def services(request):
    return HttpResponse("this is services page")

def adminpage(request):
    return HttpResponse("this is admin page")