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
    parent = forms.ModelChoiceField(queryset=Event.objects.all(), required=False)
    rules = forms.ModelChoiceField(queryset=Rule.objects.all(), required=False)
    players = forms.ModelChoiceField(queryset=Player.objects.all(), required=False)
    start_datetime = forms.DateField(required = True, widget=forms.SelectDateWidget())
    end_datetime = forms.DateField(required = True, widget=forms.SelectDateWidget())
    #game = forms.ModelChoiceField(queryset=Game.objects.all(), required = False, widget=forms.HiddenInput())

    def __init__(self, *args, **kwargs):
        game_id = kwargs.pop('game_id','')
        super(EventForm, self).__init__(*args, **kwargs)

        #self.fields['game']=forms.ModelChoiceField(queryset=Game.objects.filter(id=game_id), widget=forms.HiddenInput())
        #self.fields['game'].value = game_id
       
    class Meta:
        model = Event
        fields = ["name", "description", "parent", "start_datetime", "end_datetime", "rules", "players"]

# class MatchForm(forms.ModelForm):
#     class Meta:
#         model = Match
#         fields = ["datetime", "rules", "players"]
