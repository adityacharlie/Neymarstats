from .models import Stats, HomeStats
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions


class NeyStatsForm(forms.ModelForm):

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
        exclude = ['homestats']

class NeyHomeStatsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(NeyHomeStatsForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-4'
        self.helper.field_class = 'col-lg-8'
        self.helper.form_id = 'id-neymarhomestatform'
        

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
            'home_rating',
            FormActions(
                Submit('save_changes', 'Save changes', css_class="btn-primary"),
                Submit('cancel', 'Cancel'),
            ),
        )

    class Meta:
        model = HomeStats
        exclude = ['pub_date']

    