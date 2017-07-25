# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Point(models.Model):
    allocation = models.IntegerField(default=0)

class Participant(models.Model):
    full_name = models.CharField(max_length=128)

class Rule(models.Model):
    description = models.CharField(max_length=128, default="N/A")
    beneficiary = models.ForeignKey(Participant, null=True)
    point = models.ForeignKey(Point, null=True)

class Game(models.Model):
    name = models.CharField(max_length=128)
    rules = models.ManyToManyField(Rule)

class Event(models.Model):
    participants = models.ManyToManyField(Participant)
    name = models.CharField(max_length=128)
    rules = models.ManyToManyField(Rule)

class Encounter(models.Model):
    participants = models.ManyToManyField(Participant)
    rules = models.ManyToManyField(Rule)
    datetime = models.DateTimeField()
    

    

# class Influence(models.Model):
#     pass
