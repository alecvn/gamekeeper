# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponseRedirect, reverse
from forms import EventForm
from models import Event

def index(request):
    event_form = EventForm()
    events = Event.objects.all()
    
    return render(request, "encounters/index.html", {'event_form': event_form, 'events': events})

def new(request):
    event_form = EventForm()
    
    return render(request, "encounters/index.html", {'event_form': event_form})

def create(request):
    event_form = EventForm(request.POST)
    if event_form.is_valid():
        event_form.save()
        return HttpResponseRedirect(reverse('index'))
    return render(request, 'encounters/index.html', {
        'error_message': event_form.errors
    })
    

def edit(request):
    return HttpResponse("Modify now")

def update(request):
    return HttpResponse("Update now")
