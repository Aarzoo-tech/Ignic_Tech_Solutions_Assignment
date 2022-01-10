from django.http import request
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from ImageAction.models import addEvent
from django.http.response import HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect
@csrf_protect
def eventsAdd(request):
    if request.method=='POST':
        eventData=request.POST
        eventObject=addEvent()
        eventObject.event_name=eventData['eventname']
        eventObject.date=eventData['eventdate']
        eventObject.time=eventData['eventtime']
        eventObject.location=eventData['eventlocation']
        eventObject.image=request.FILES.get('eventimage')
        eventObject.save()
        return redirect("http://localhost:8000/show-events")
    return render(request,'AddEvent.html')
def showEvents(request):
    eventslist=addEvent.objects.all()
    return render(request,'showEvents.html',{'eventslist':eventslist})