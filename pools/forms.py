from .models import AwayStats, HomeStats
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit, Div, HTML
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions


"""class NeyStatsForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(NeyStatsForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-4'
        self.helper.field_class = 'col-lg-8'
        self.helper.form_id = 'id-neymarstatform'
        

        self.helper.layout = Layout(
            Field('game_appearences', css_class='input-xlarge'),
            Field('minutes_played', css_class='input-xlarge'),
            'goals_scored',
            'assists',
            'yellow_cards',
            'red_cards', 
            'shots_per_game',
            'pass_success_percentage',
            'aerials_won',
            'man_of_the_match',
            'overall_rating',
            FormActions(
                Submit('save_changes', 'Save changes', css_class="btn-primary"),
                Submit('cancel', 'Cancel'),
            ),
        )

    class Meta:
        model = Stats
        exclude = ['homestats']"""

class NeyHomeStatsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(NeyHomeStatsForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-8'
        self.helper.field_class = 'col-lg-4'
        #self.helper.form_id = 'id-neymarhomestatform'
        self.helper.form_id = 'id-neymarhomestatform'
        

        self.helper.layout = Layout(
            Div(
                HTML("<p>Home</p>"),
            ),
            Field('game_appearences', css_class='input-xlarge'),
            Field('minutes_played', css_class='input-xlarge'),
            'goals_scored',
            'assists',
            'yellow_cards',
            'red_cards', 
            'shots_per_game',
            'pass_success_percentage',
            'aerials_won',
            'man_of_the_match',
            'home_rating',
            FormActions(
                Submit('save', 'Save', css_class="btn-primary", name='home_submit'),
                Submit('cancel', 'Cancel'),
            ),
        )

    class Meta:
        model = HomeStats
        exclude = ['awaystats','created_at','updated_at']


class NeyAwayStatsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(NeyAwayStatsForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.field_class = 'col-lg-4'
        self.helper.form_id = 'id-neymarawaystatform'
        self.helper.form_show_labels = False
        #I am not sure if this stays here

        self.helper.layout = Layout(
            Div(
                HTML("<p>Away</p>"),
            ),
            Field('game_appearences', css_class='input-xlarge'),
            Field('minutes_played', css_class='input-xlarge'),
            'goals_scored',
            'assists',
            'yellow_cards',
            'red_cards', 
            'shots_per_game',
            'pass_success_percentage',
            'aerials_won',
            'man_of_the_match',
            'away_rating',
            FormActions(
                Submit('save', 'Save', css_class="btn-primary", name='away_submit'),
                Submit('cancel', 'Cancel'),
            ),
        )

    class Meta:
        model = AwayStats
        exclude = ['away_rating','created_at','updated_at']       

    

#https://stackoverflow.com/questions/34317157/multiple-django-crispy-forms-in-one-view
# both form validations are being run no matter which submit button is pressed

