import datetime

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def welcome(request):
    return render(request, 'website/welcome.html',
                  {'message': 'this data is from def welcome'})


def date(request):
    return HttpResponse("this page was server at " + str(datetime.datetime.now()))

