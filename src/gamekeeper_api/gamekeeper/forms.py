from django import forms
from models import Event, Game, Player, Rule, Point, Action

class PointForm(forms.ModelForm):
    class Meta:
        model = Point
        fields = ["allocation"]

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ["full_name"]

class RuleForm(forms.ModelForm):
    class Meta:
        model = Rule
        fields = ["description", "point"]

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ["name", "rules"]

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ["name", "rules", "players"]

# class MatchForm(forms.ModelForm):
#     class Meta:
#         model = Match
#         fields = ["datetime", "rules", "players"]
