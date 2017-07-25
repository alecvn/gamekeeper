from django import forms
from models import Event, Game, Participant, Rule, Point, Encounter

class PointForm(forms.ModelForm):
    class Meta:
        model = Point
        fields = ["allocation"]

class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ["full_name"]

class RuleForm(forms.ModelForm):
    class Meta:
        model = Rule
        fields = ["description", "beneficiary", "point"]

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ["name", "rules"]

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ["name", "rules", "participants"]

class EncounterForm(forms.ModelForm):
    class Meta:
        model = Encounter
        fields = ["datetime", "rules", "participants"]

