import datetime

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def welcome(request):
    return HttpResponse("Welcome to the metting planer")

def date(request):
    return HttpResponse("this page was server at " + str(datetime.datetime.now()))

