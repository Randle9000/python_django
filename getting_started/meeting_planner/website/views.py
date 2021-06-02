import datetime

from django.shortcuts import render
from django.http import HttpResponse
from meetings.models import Meeting

# Create your views here.
def welcome(request):
    return render(request, 'website/welcome.html',
                  {'message': 'template variable this data is from def welcome',
                   'x': 42,
                   'num_meetings': Meeting.objects.count()}
                  )


def date(request):
    return HttpResponse("this page was server at " + str(datetime.datetime.now()))

