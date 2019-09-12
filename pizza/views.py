from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1>Top Text</h1>")

def komunikat(request):
    return HttpResponse("<h1>Bottom Text</h1>")

def tak(request):
    return HttpResponse("<h1>Middle Text</h1>")