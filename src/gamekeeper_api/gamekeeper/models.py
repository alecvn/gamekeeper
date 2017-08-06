# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


def comp(list1, list2):
    copy_list1 = list(list1)
    copy_list2 = list(list2)

    for val in list1:
        if val in copy_list2:
            copy_list1.remove(val)
            copy_list2.remove(val)
    return len(copy_list1) == 0

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
        results = ActionResult.objects.filter(event_id=event.id, player_id=player.id, action_id=self.id)
        if len(results) == 0:
            for child_action in self.children:
                for child_event in event.children:
                    child_results = ActionResult.objects.filter(event_id=child_event.id, player_id=player.id, action_id=child_action.id)
                    if len(child_results) > 0:
                        children_with_results.append(child_results[0])

            if len(self.children) > 0:
                if len(children_with_results) == len(self.children):
                    result = ActionResult.objects.create(event=event, player=player, action=self)
                else:
                    for child in self.children:
                        for child_event in event.children:
                            child.evaluate_children(child_event, player)


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

    @staticmethod
    def get_deep_triggered_rules_for_player_and_event(player, event):
        triggered_rules = []

        for child_event in event.get_all_children():
            triggered_rules += Rule.get_triggered_rules_for_player_and_event(player, child_event)
        return triggered_rules

    
    
    @staticmethod
    def get_triggered_rules_for_player_and_event(player, event):
        triggered_rules = []
        action_results = []
        rules = event.rules.all()
        for child_event in event.children:
            action_results += ActionResult.objects.filter(player=player, event=child_event)
        # if player.full_name == "Zaheer":
        #     import pdb;pdb.set_trace()
    
        for rule in rules:
            triggers = Trigger.objects.filter(rule=rule)
            triggers_list = map(lambda trigger: trigger.action, triggers)
            player_actions = map(lambda result: result.action, action_results)
            
            # if len(player_actions) > 0:
            # if player.full_name == "Tshepo":
                #import pdb;pdb.set_trace()

            if comp(triggers_list, player_actions):
                triggered_rules.append(rule)
        
        return triggered_rules

#        return sum(map(lambda x: x.rule.point.allocation, RuleResult.get_deep_rules_for_event_and_player(main_event, player)))

class Player(models.Model):
    full_name = models.CharField(max_length=128)
    points = models.ManyToManyField(Point, blank=True)
    actions = models.ManyToManyField(Action, blank=True)
    rules = models.ManyToManyField(Rule, blank=True)

    def __unicode__(self):
        return self.full_name

    @property
    def rules_triggered(self):
        triggered_rules = []
        events = Event.objects.filter(parent_id__isnull=True)
        for event in events:
            triggered_rules += Rule.get_deep_triggered_rules_for_player_and_event(self, event)
        return triggered_rules

    @property
    def actions_triggered(self):
        triggered_actions = []
        events = Event.objects.filter(parent_id__isnull=True)
        for event in events:
            child_events = event.get_all_children()
            for child_event in child_events:
                triggered_actions += ActionResult.objects.filter(player=self, event=child_event)
        return triggered_actions

    def total_points(self, event):
        event = Event.objects.get(pk=event.id)
        triggered_rules = Rule.get_deep_triggered_rules_for_player_and_event(self, event)

        return sum(map(lambda rule: rule.point.allocation, triggered_rules))

    
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

    def get_all_children(self):
        children = [self]
        try:
            child_list = self.children.all()
        except AttributeError:
            return children
        for child in child_list:
            children.extend(child.get_all_children())
        return children

        # children = []
        # for child in self.child_events.all():
        #     children.append(child.get_all_children())
        # return children

    @property
    def players_list(self):
        return self.players.all()

    @property
    def action_list(self):
        return self.actions.all()


class ActionResult(models.Model):
    event = models.ForeignKey(Event, related_name="action_results")
    action = models.ForeignKey(Action, related_name="action_results")
    player = models.ForeignKey(Player, related_name="action_results")
    description = models.CharField(max_length=128, null=True, blank=True)

    def __unicode__(self):
        return u'{0} - {1} - {2} - {3}'.format(self.player.full_name, self.event.name, self.action.description, self.description)

    @staticmethod
    def get_actions_for_event_and_player(event, player):
        results = ActionResult.objects.filter(event=event, player=player)
        if len(results) > 0:
            return map(lambda x: x.action, results)

    @staticmethod
    def get_deep_actions_for_event_and_player(event, player):
        actions = []
        for child_event in event.get_all_children():
            actions += ActionResult.actions_for_event_and_player(child_event, player)
        return actions


class RuleResult(models.Model):
    event = models.ForeignKey(Event, related_name="rule_results")
    rule = models.ForeignKey(Rule, related_name="rule_results")
    player = models.ForeignKey(Player, related_name="rule_results")
    description = models.CharField(max_length=128, null=True, blank=True)

    def __unicode__(self):
        return u'{0} - {1} - {2}'.format(self.player.full_name, self.event.name, self.action.description)

    @staticmethod
    def get_rules_for_event_and_player(event, player):
        results = RuleResult.objects.filter(event=event, player=player)
        if len(results) > 0:
            return map(lambda x: x.rule, results)

    @staticmethod
    def get_deep_rules_for_event_and_player(event, player):
        rules = []
        for child_event in event.get_all_children():
            actions += RuleResult.rules_for_event_and_player(child_event, player)
        return rules
        

# class Result(models.Model):
#     pass
