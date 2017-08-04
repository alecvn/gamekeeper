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
    def children(self):
        return self.child_actions.all()

class Player(models.Model):
    full_name = models.CharField(max_length=128)
    points = models.ManyToManyField(Point)
    actions = models.ManyToManyField(Action)

    def __unicode__(self):
        return self.full_name

    @property
    def total(self):
        points = list(map(lambda x: x.action.point.allocation if x.action.point else 0, self.outcomes.all()))
        return sum(points)
    
class Rule(models.Model):
    # rules look at a state at any given time and deduce when and where it is triggered
    # allow to look at log of events or actions as they happen
    parent = models.ForeignKey("self", null=True)
    description = models.CharField(max_length=128, default="N/A")
    triggering_action = models.ForeignKey(Action, null=True, related_name="triggered_rules")
    triggered_action = models.ForeignKey(Action, null=True, related_name="triggering_rules")
    point = models.ForeignKey(Point, null=True)

    def __unicode__(self):
        return self.description

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

class Outcome(models.Model):
    event = models.ForeignKey(Event)
    actions = models.ManyToManyField(Action)
    player = models.ForeignKey(Player, related_name="outcomes")

# class Match(models.Model):
#     event = models.ForeignKey(Event)
#     players = models.ManyToManyField(Player)
#     rules = models.ManyToManyField(Rule)
#     start_datetime = models.DateTimeField()
#     end_datetime = models.DateTimeField()

# class Game(models.Model):
#     match = models.ForeignKey(Match)
#     players = models.ManyToManyField(Player)
#     rules = models.ManyToManyField(Rule)
#     datetime = models.DateTimeField()
#     start_datetime = models.DateTimeField()
#     end_datetime = models.DateTimeField()
