# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Point(models.Model):
    description = models.CharField(max_length=128)
    allocation = models.IntegerField(default=0)

    def __unicode__(self):
        return u'{0} - {1}'.format(self.description, self.allocation)

class Action(models.Model):
    parent = models.ForeignKey("self", null=True, blank=True, related_name="child_actions")
    description = models.CharField(max_length=128)
    point = models.ForeignKey(Point, null=True, blank=True)

    def __unicode__(self):
        return self.description

    @property
    def results_list(self):
        return self.results.all()

    @property
    def children(self):
        return self.child_actions.all()

    def evaluate_children(self, event, player):
        children_with_results = []
        results = PlayerEventAction.objects.filter(event_id=event.id, player_id=player.id, action_id=self.id)
        if len(results) == 0:
            for child_action in self.children:
                for child_event in event.children:
                    child_results = PlayerEventAction.objects.filter(event_id=child_event.id, player_id=player.id, action_id=child_action.id)
                    if len(child_results) > 0:
                        children_with_results.append(child_results[0])

            if len(self.children) > 0:
                if len(children_with_results) == len(self.children):
                    result = PlayerEventAction.objects.create(event=event, player=player, action=self)
                else:
                    for child in self.children:
                        for child_event in event.children:
                            child.evaluate_children(child_event, player)


class Player(models.Model):
    full_name = models.CharField(max_length=128)
    points = models.ManyToManyField(Point, blank=True)
    actions = models.ManyToManyField(Action, blank=True)

    def __unicode__(self):
        return self.full_name

    @property
    def total(self):
        points = list(map(lambda x: x.action.point.allocation if x.action.point else 0, self.results.all()))
        return sum(points)
    
class Rule(models.Model):
    # rules look at a state at any given time and deduce when and where it is triggered
    # allow to look at log of events or actions as they happen
    parent = models.ForeignKey("self", null=True, blank=True)
    description = models.CharField(max_length=128, default="N/A")
    point = models.ForeignKey(Point, null=True)
    triggers = models.ManyToManyField(Action, through="Trigger")

    def __unicode__(self):
        return self.description

    @property
    def trigger_list(self):
        return Trigger.objects.filter(rule_id=self.id)

class Trigger(models.Model):
    rule = models.ForeignKey(Rule)
    action = models.ForeignKey(Action)

    def __unicode__(self):
        return "{0}".format(self.action.description)

class Game(models.Model):
    name = models.CharField(max_length=128)
    actions = models.ManyToManyField(Action, blank=True)

    def __unicode__(self):
        return self.name

class Event(models.Model):
    # events can be a league, series, match or a game
    # start and end datetime can either be realtime or set.  they can either be limits or recorded in other words.
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=128, null=True, blank=True)
    game = models.ForeignKey(Game)
    parent = models.ForeignKey("self", null=True, blank=True, related_name="child_events")
    players = models.ManyToManyField(Player)
    rules = models.ManyToManyField(Rule, blank=True)
    actions = models.ManyToManyField(Action)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()

    def __unicode__(self):
        return self.name

    @property
    def children(self):
        return self.child_events.all()

    @property
    def players_list(self):
        return self.players.all()

    @property
    def action_list(self):
        return self.actions.all()

class PlayerEventAction(models.Model):
    event = models.ForeignKey(Event, related_name="player_event_actions")
    action = models.ForeignKey(Action, related_name="player_event_actions")
    player = models.ForeignKey(Player, related_name="player_event_actions")

    def __unicode__(self):
        return u'{0} - {1} - {2}'.format(self.player.full_name, self.event.name, self.action.description)

# class Result(models.Model):
#     pass
