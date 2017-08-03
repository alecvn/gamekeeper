# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponseRedirect, reverse
from forms import EventForm, GameForm, PlayerForm, RuleForm, PointForm#, MatchForm
from models import Event, Game, Player, Rule, Point#, Match

def list_games(request):
    game_form = GameForm()
    games = Game.objects.all()

    return render(request, "gamekeeper/index.html", {'game_form': game_form, 'games': games})

def new_game(request):
    game_form = GameForm()

    return render(request, "gamekeeper/index.html", {'game_form': game_form})

def create_game(request):
    game_form = GameForm(request.POST)
    if game_form.is_valid():
        game_form.save()
        return HttpResponseRedirect(reverse('list_games'))
    return render(request, 'gamekeeper/index.html', {
        'error_message': game_form.errors
    })

def list_participants(request):
    participant_form = PlayerForm()
    participants = Player.objects.all()
    
    return render(request, "gamekeeper/index.html", {'participant_form': participant_form, 'participants': participants})

def new_participant(request):
    participant_form = PlayerForm()
    
    return render(request, "gamekeeper/index.html", {'participant_form': participant_form})

def create_participant(request):
    participant_form = PlayerForm(request.POST)
    if participant_form.is_valid():
        participant_form.save()
        return HttpResponseRedirect(reverse('index'))
    return render(request, 'gamekeeper/index.html', {
        'error_message': participant_form.errors
    })

def list_rules(request):
    rule_form = RuleForm()
    rules = Rule.objects.all()

    return render(request, "gamekeeper/rules_index.html", {'rule_form': rule_form, 'rules': rules})

def new_rule(request):
    rule_form = RuleForm()
    
    return render(request, "gamekeeper/rules_index.html", {'rule_form': rule_form})

def create_rule(request):
    rule_form = RuleForm(request.POST)
    if rule_form.is_valid():
        rule_form.save()
        return HttpResponseRedirect(reverse('list_rules'))
    return render(request, 'gamekeeper/rules_index.html', {
        'error_message': rule_form.errors
    })

# def list_matches(request):
#     encounter_form = MatchForm()
#     gamekeeper = Match.objects.all()
    
#     return render(request, "gamekeeper/index.html", {'encounter_form': encounter_form, 'gamekeeper': gamekeeper})

# def new_match(request):
#     encounter_form = MatchForm()
    
#     return render(request, "gamekeeper/index.html", {'encounter_form': encounter_form})

# def create_match(request):
#     encounter_form = MatchForm(request.POST)
#     if encounter_form.is_valid():
#         encounter_form.save()
#         return HttpResponseRedirect(reverse('index'))
#     return render(request, 'gamekeeper/index.html', {
#         'error_message': encounter_form.errors
#     })

def list_events(request, game_id):
    event_form = EventForm(game_id=game_id)
    parent_events = Event.objects.filter(parent_id__isnull=True, game_id=game_id)
    
    return render(request, "gamekeeper/events_index.html", {'event_form': event_form, 'parent_events': parent_events, 'game_id': game_id})

def new_event(request):
    event_form = EventForm()
    
    return render(request, "gamekeeper/index.html", {'event_form': event_form})

def show_event(request, game_id, event_id):
    event = Event.objects.get(event_id)
    
    return render(request, "gamekeeper/show_event.html", {'event': event, 'game_id': game_id})

def create_event(request, game_id):
    event_form = EventForm(request.POST, game_id=game_id)
    if event_form.is_valid():
        event_form.cleaned_data['game_id'] = game_id
        event_form.save()
        return HttpResponseRedirect(reverse('events_index', game_id))
    return render(request, 'gamekeeper/events_index.html', {
        'error_message': event_form.errors,
        'game_id': game_id
    })

def list_players(request):
    player_form = PlayerForm()
    players = Player.objects.all()
    
    return render(request, "gamekeeper/players_index.html", {'player_form': player_form, 'players': players})

def new_player(request):
    player_form = PlayerForm()
    
    return render(request, "gamekeeper/players_index.html", {'player_form': player_form})

def create_player(request):
    player_form = PlayerForm(request.POST)
    if player_form.is_valid():
        player_form.save()
        return HttpResponseRedirect(reverse('list_players'))
    return render(request, 'gamekeeper/players_index.html', {
        'error_message': player_form.errors
    })
