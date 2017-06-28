# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Participant(models.Model):
    full_name = models.CharField(max_length=128)


class Event(models.Model):
    name = models.CharField(max_length=128)


class Encounter(models.Model):
    pass


class Rule(models.Model):
    encounter = models.ForeignKey()


class Point(models.Model):
    pass

