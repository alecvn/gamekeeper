# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponseRedirect, reverse
from forms import EventForm, GameForm, PlayerForm, RuleForm, PointForm, ActionForm
from models import Event, Game, Player, Rule, RuleResult, Point, Action, ActionResult, Trigger

def list_games(request):
    game_form = GameForm()
    games = Game.objects.all()

    return render(request, "gamekeeper/games_index.html", {'game_form': game_form, 'games': games})

def create_game(request):
    game_form = GameForm(request.POST)
    if game_form.is_valid():
        game_form.save()
        return HttpResponseRedirect(reverse('list_games'))
    return render(request, 'gamekeeper/games_index.html', {
        'error_message': game_form.errors
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
    event_to_clone_id = request.POST['event_to_clone_id']
    if not event_to_clone_id:
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
    else:
        event_to_clone = Event.objects.get(pk=event_to_clone_id)
        new_event = Event.objects.create(name=request.POST['name'], parent=event_to_clone.parent, game=event_to_clone.game, start_datetime=event_to_clone.start_datetime, end_datetime=event_to_clone.end_datetime)
        for rule in event_to_clone.rules.all():
            new_event.rules.add(rule)
        for child_event in event_to_clone.child_events.all():
            new_child_event = Event.objects.create(name=child_event.name, game=event_to_clone.game, start_datetime=event_to_clone.start_datetime, end_datetime=event_to_clone.end_datetime)
            new_event.child_events.add(new_child_event)
            for action in child_event.actions.all():
                new_child_event.actions.add(action)
        return HttpResponseRedirect(reverse('list_events', kwargs={'game_id': game_id}))
        

def update_event(request, game_id, event_id):
    player_to_add_id = request.POST['player_to_add_id']
    action_to_add_id = request.POST['action_to_add_id']
    rule_to_add_id = request.POST['rule_to_add_id']
    remove_rule = request.POST['remove_rule'] if 'remove_rule' in request.POST else False

    if player_to_add_id != "":
        player_to_add = Player.objects.get(pk=player_to_add_id)
        event = Event.objects.get(pk=event_id)
        event.players.add(player_to_add)
        for child_event in event.children.all():
            child_event.players.add(player_to_add)
    elif action_to_add_id != "":
        action_to_add = Action.objects.get(pk=action_to_add_id)
        event = Event.objects.get(pk=event_id)
        event.actions.add(action_to_add)
    elif rule_to_add_id != "":
        rule_to_add = Rule.objects.get(pk=rule_to_add_id)
        event = Event.objects.get(pk=event_id)
        event.rules.add(rule_to_add)
    elif remove_rule:
        rule_to_remove = Rule.objects.get(pk=remove_rule)
        event = Event.objects.get(pk=event_id)
        event.rules.remove(rule_to_remove)
    else:
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

def react(request):
    return render(request, "gamekeeper/index.html")





from rest_framework import status, serializers, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

class ActionResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActionResult
        fields = ('description', 'action', 'event', 'player',)

    def create(self, validated_data):
        action_result = ActionResult.objects.create(description=validated_data['description'], action=validated_data['action'], player=validated_data['player'], event=validated_data['event'])
        return action_result
    
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions

@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def action_result_list(request):
    """
    List all action results, or create a new action result.
    """
    if request.method == 'GET':
        action_results = ActionResult.objects.all()
        serializer = ActionResultSerializer(action_results, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ActionResultSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def clone_event(request):
    """
    Clone event
    """
    if request.method == 'POST':
        event = Event.clone(request.data['name'])
        serializer = EventSerializer(event)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class PlayerSerializer(serializers.ModelSerializer):
    points = serializers.SerializerMethodField('calculate_points')

    def calculate_points(self, obj):
        return obj.points_for_event(self.context.get('event'))
    
    class Meta:
        model = Player
        fields = ('id', 'full_name', 'points',)

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def player_event_context(request, event_id):
     if request.method == 'GET':
        event = Event.objects.get(pk=event_id)
        players = event.players#.filter(pk=player_id)
        serializer = PlayerSerializer(players, many=True, context={'event': event})
        return Response(serializer.data)


class EventSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        event = Event.objects.create(name=validated_data['name'],
                                     parent=validated_data['parent'],
                                     start_datetime=validated_data['start_datetime'],
                                     end_datetime=validated_data['end_datetime'],
                                     game=validated_data['game'])
        for child in validated_data['child_events']:
            event.child_events.add(child)
        for player in validated_data['players']:
            event.players.add(player)
        for action in validated_data['actions']:
            event.actions.add(action)
        for rule in validated_data['rules']:
            event.rules.add(rule)
        return event

    class Meta:
        model = Event
        fields = ('id', 'name', 'players_points', 'game',
                  'actions', 'players', 'rules', 'parent',
                  'child_events','start_datetime','end_datetime')

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all().prefetch_related('players__actions',
                                                    'rules__triggers',
                                                    'child_events')
    serializer_class = EventSerializer
