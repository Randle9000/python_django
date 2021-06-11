from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello There')

def detail(request):
    return HttpResponse("Hello There this is detail page")