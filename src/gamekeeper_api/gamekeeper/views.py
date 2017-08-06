# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponseRedirect, reverse
from forms import EventForm, GameForm, PlayerForm, RuleForm, PointForm, ActionForm
from models import Event, Game, Player, Rule, RuleResult, Point, Action, ActionResult, Trigger

def list_games(request):
    game_form = GameForm()
    games = Game.objects.all()

    return render(request, "gamekeeper/index.html", {'game_form': game_form, 'games': games})

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

def show_rule(request, rule_id):
    rule = Rule.objects.get(pk=rule_id)
    actions = Action.objects.all()
    return render(request, "gamekeeper/rule_show.html", {'rule': rule, 'actions': actions, 'rule_id': rule.id})

def update_rule(request, rule_id):
    trigger_id = request.POST['trigger']
    rule = Rule.objects.get(pk=rule_id)
    action = Action.objects.get(pk=trigger_id)

    trigger = Trigger.objects.create(rule=rule, action=action)

    return HttpResponseRedirect(reverse('show_rule', kwargs={'rule_id': rule_id}))

def create_rule(request):
    rule_form = RuleForm(request.POST)
    if rule_form.is_valid():
        rule_form.save()
        return HttpResponseRedirect(reverse('list_rules'))
    return render(request, 'gamekeeper/rules_index.html', {
        'error_message': rule_form.errors
    })

def list_events(request, game_id):
    event_form = EventForm()
    parent_events = Event.objects.filter(parent_id__isnull=True)

    return render(request, "gamekeeper/events_index.html", {'event_form': event_form, 'parent_events': parent_events, 'game_id': game_id})

def show_event(request, game_id, event_id):
    event = Event.objects.get(pk=event_id)
    results = ActionResult.objects.filter(event_id=event.id)
    rules = event.rules.all()
    return render(request, "gamekeeper/event_show.html", {'event': event, 'rules': rules, 'results': results, 'game_id': game_id, 'event_id': event.id})

def create_event(request, game_id):
    event_form = EventForm(request.POST)

    if event_form.is_valid():
        event = event_form.save(commit=False)
        event.game_id = game_id
        event.save()
        event_form.save_m2m()
        return HttpResponseRedirect(reverse('list_events', kwargs={'game_id': game_id}))
    return render(request, 'gamekeeper/events_index.html', {
        'error_message': event_form.errors,
        'game_id': game_id
    })

def update_event(request, game_id, event_id):
    result_params = request.POST['result']

    action_id, player_id = result_params.split(",")
    action = Action.objects.get(pk=action_id)
    player = Player.objects.get(pk=player_id)

    description = request.POST['description%s' % player_id]

    event = Event.objects.get(pk=event_id)
    if description:
        ActionResult.objects.create(event=event, player=player, action=action, description=description)
    else:
        ActionResult.objects.create(event=event, player=player, action=action)

    return HttpResponseRedirect(reverse('show_event', kwargs={'game_id': game_id, 'event_id': event_id}))

def list_players(request):
    player_form = PlayerForm()
    players = Player.objects.all()
    
    return render(request, "gamekeeper/players_index.html", {'player_form': player_form, 'players': players})

def create_player(request):
    player_form = PlayerForm(request.POST)
    if player_form.is_valid():
        player_form.save()
        return HttpResponseRedirect(reverse('list_players'))
    return render(request, 'gamekeeper/players_index.html', {
        'error_message': player_form.errors
    })

def list_actions(request):
    action_form = ActionForm()
    parent_actions = Action.objects.filter(parent_id__isnull=True)
    
    return render(request, "gamekeeper/actions_index.html", {'action_form': action_form, 'parent_actions': parent_actions})

def evaluate_actions(request, game_id, event_id):
    # eventually filter by event and player here
    parent_event = Event.objects.get(pk=event_id)

    for event in parent_event.children:
        rules = event.rules.all()
        if len(rules) > 0:
            for rule in rules:
                action_results = []
                for child_event in event.children:
                    for player in child_event.players.all():
                        peas = ActionResult.objects.filter(event=child_event, player=player)
                        for pea in peas:
                            action_results.append(pea)

                if list(rule.triggers.all()) == map(lambda x: x.action, action_results):
                    action_results[0].player.rules.add(rule)
    # actions = event.actions.filter(parent_id__isnull=True)
    # # TODO: fix this hack
    # if len(actions) == 0:
    #     event = event.children[0]
    #     actions = event.actions.all()

    # players = event.players.all()

    # for player in players:
    #     for action in actions:
    #         action.evaluate_children(event, player)

    return HttpResponseRedirect(reverse('list_results', kwargs={'game_id': game_id, 'event_id': event_id}))

def create_action(request):
    action_form = ActionForm(request.POST)
    if action_form.is_valid():
        action_form.save()
        # action, created = Action.objects.get_or_create(**action_form.cleaned_data)
        return HttpResponseRedirect(reverse('list_actions'))
    return render(request, 'gamekeeper/actions_index.html', {
        'error_message': action_form.errors
    })

def list_points(request):
    point_form = PointForm()
    points = Point.objects.all()
    
    return render(request, "gamekeeper/points_index.html", {'point_form': point_form, 'points': points})

def create_point(request):
    point_form = PointForm(request.POST)
    if point_form.is_valid():
        point_form.save()
        return HttpResponseRedirect(reverse('list_points'))
    return render(request, 'gamekeeper/points_index.html', {
        'error_message': point_form.errors
    })

def list_results(request, game_id, event_id):
    event = Event.objects.get(pk=event_id)
    players = event.players.all()
    points = map(lambda player: player.total_points(event), players)

    return render(request, "gamekeeper/results_index.html", {'players': players, 'points': points, 'game_id': game_id, 'event_id': event_id})
