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
        results = Result.objects.filter(event_id=event.id, player_id=player.id, action_id=self.id)
        if len(results) == 0:
            import pdb;pdb.set_trace()
            for child in self.children:
                child_results = Result.objects.filter(event_id=event.id, player_id=player.id, action_id=child.id)
                if len(child_results) > 0:
                    children_with_results.append(child_results[0])

            if len(children_with_results) == len(self.children):
                result = Result.objects.create(event=event, player=player, action=self)
            else:
                for child in self.children:
                    child.evaluate_children(event, player)

        # if reduce(lambda arr, child: len(Result.objects.filter(event_id=event.id, player_id=player.id, action_id=child.id)) == 1, self.children, []):
        #     result = Result.objects.create(event=event, player=player, action=self)
        

    # @staticmethod
    # def evaluate_all(event_id, player_id):
    #     # pass event_id through here
    #     actions = Action.objects.filter(parent_id__isnull=True)
    #     for action in actions:
    #         action.evaluate_children()


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

class Result(models.Model):
    event = models.ForeignKey(Event, related_name="results")
    action = models.ForeignKey(Action, related_name="results")
    player = models.ForeignKey(Player, related_name="results")

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
