# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponseRedirect, reverse
from forms import EventForm, GameForm, ParticipantForm, RuleForm, PointForm, EncounterForm
from models import Event, Game, Participant, Rule, Point, Encounter

def list_games(request):
    game_form = GameForm()
    games = Game.objects.all()
    
    return render(request, "encounters/index.html", {'game_form': game_form, 'games': games})

def new_game(request):
    game_form = GameForm()
    
    return render(request, "encounters/index.html", {'game_form': game_form})

def create_game(request):
    game_form = GameForm(request.POST)
    if game_form.is_valid():
        game_form.save()
        return HttpResponseRedirect(reverse('index'))
    return render(request, 'encounters/index.html', {
        'error_message': game_form.errors
    })

def list_participants(request):
    participant_form = ParticipantForm()
    participants = Participant.objects.all()
    
    return render(request, "encounters/index.html", {'participant_form': participant_form, 'participants': participants})

def new_participant(request):
    participant_form = ParticipantForm()
    
    return render(request, "encounters/index.html", {'participant_form': participant_form})

def create_participant(request):
    participant_form = ParticipantForm(request.POST)
    if participant_form.is_valid():
        participant_form.save()
        return HttpResponseRedirect(reverse('index'))
    return render(request, 'encounters/index.html', {
        'error_message': participant_form.errors
    })

def list_rules(request):
    rule_form = RuleForm()
    rules = Rule.objects.all()
    
    return render(request, "encounters/index.html", {'rule_form': rule_form, 'rules': rules})

def new_rule(request):
    rule_form = RuleForm()
    
    return render(request, "encounters/index.html", {'rule_form': rule_form})

def create_rule(request):
    rule_form = RuleForm(request.POST)
    if rule_form.is_valid():
        rule_form.save()
        return HttpResponseRedirect(reverse('index'))
    return render(request, 'encounters/index.html', {
        'error_message': rule_form.errors
    })

def list_encounters(request):
    encounter_form = EncounterForm()
    encounters = Encounter.objects.all()
    
    return render(request, "encounters/index.html", {'encounter_form': encounter_form, 'encounters': encounters})

def new_encounter(request):
    encounter_form = EncounterForm()
    
    return render(request, "encounters/index.html", {'encounter_form': encounter_form})

def create_encounter(request):
    encounter_form = EncounterForm(request.POST)
    if encounter_form.is_valid():
        encounter_form.save()
        return HttpResponseRedirect(reverse('index'))
    return render(request, 'encounters/index.html', {
        'error_message': encounter_form.errors
    })

def list_events(request):
    event_form = EventForm()
    events = Event.objects.all()
    
    return render(request, "encounters/index.html", {'event_form': event_form, 'events': events})

def new_event(request):
    event_form = EventForm()
    
    return render(request, "encounters/index.html", {'event_form': event_form})

def create_event(request):
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
