# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Point(models.Model):
    allocation = models.IntegerField(default=0)

class Player(models.Model):
    full_name = models.CharField(max_length=128)

class Rule(models.Model):
    description = models.CharField(max_length=128, default="N/A")
    beneficiary = models.ForeignKey(Player, null=True)
    point = models.ForeignKey(Point)

class Game(models.Model):
    name = models.CharField(max_length=128)
    rules = models.ManyToManyField(Rule, blank=True)

class Event(models.Model):
    game = models.ForeignKey(Game)
    players = models.ManyToManyField(Player)
    name = models.CharField(max_length=128)
    rules = models.ManyToManyField(Rule)

class Match(models.Model):
    event = models.ForeignKey(Event)
    players = models.ManyToManyField(Player)
    rules = models.ManyToManyField(Rule)
    datetime = models.DateTimeField()
