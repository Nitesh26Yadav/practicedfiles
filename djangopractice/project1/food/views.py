from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse(" Hello World ")
    
def item(request):
    return HttpResponse('<h1>This is the Item view</h1>')

def favoriteitems(request):
    return HttpResponse('This is your favorites Items.')