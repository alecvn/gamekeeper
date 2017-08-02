# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Point(models.Model):
    description = models.CharField(max_length=128)
    allocation = models.IntegerField(default=0)

class Player(models.Model):
    full_name = models.CharField(max_length=128)
    points = models.ManyToManyField(Point)
    
class Action(models.Model):
    description = models.CharField(max_length=128)
    triggering_player = models.ForeignKey(Player)

class Rule(models.Model):
    # rules look at a state at any given time and deduce when and where it is triggered
    # allow to look at log of events or actions as they happen
    parent = models.ForeignKey("self", null=True)
    description = models.CharField(max_length=128, default="N/A")
    action = models.ForeignKey(Action)
    point = models.ForeignKey(Point, null=True)

class Game(models.Model):
    name = models.CharField(max_length=128)
    rules = models.ManyToManyField(Rule, blank=True)

class Event(models.Model):
    # events can be a league, series, match or a game
    # start and end datetime can either be realtime or set.  they can either be limits or recorded in other words.
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=128, null=True)
    game = models.ForeignKey(Game)
    parent = models.ForeignKey("self", null=True)
    players = models.ManyToManyField(Player)
    rules = models.ManyToManyField(Rule)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()

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
