from django.shortcuts import render, get_object_or_404, redirect
from django.forms import modelform_factory

from .models import Meeting, Room

def details(request, id):
    meeting = get_object_or_404(Meeting, pk=id)
    return render(request, "meetings/detail.html", {'meeting': meeting})


def rooms_details(request):
    return render(request, 'meetings/rooms_list.html',
                  {'rooms': Room.objects.all()})


MeetingForm = modelform_factory(Meeting, exclude=[]) # MeetingFrom is a class not a regula object!!


def new(request):
    if request.method == "POST":
        # a = request.POST
        # print(a)
        # print(a['title'])
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        # else is for example GET method
        form = MeetingForm() # create object
    return render(request, 'meetings/new.html',
              {'form': form})