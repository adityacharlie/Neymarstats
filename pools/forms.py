from .models import Question
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions


class QuestionForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.form_id = 'id-questionform'
    helper.form_method = 'post'
    helper.form_action = 'add_question'
        
    helper.layout = Layout(
        Field('question_text', css_class='input-xlarge'),
        Field('keywords', css_class='input-xlarge'),
        'question_type',
        'is_featured',
        'likecount',
        FormActions(
            Submit('save_changes', 'Save changes', css_class="btn-primary"),
            Submit('cancel', 'Cancel'),
        )
    #def __init__(self, *args, **kwargs):
    #    super(QuestionForm,self).__init__(*args,**kwargs)
    )

    class Meta:
        model = Question
        exclude = ['slug']