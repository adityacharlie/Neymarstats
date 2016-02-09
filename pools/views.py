from django.shortcuts import render_to_response
from .forms import QuestionForm
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

# Create your views here.


def add_question(request):
    question_form = QuestionForm()
    if request.method == 'POST':
        question_form = QuestionForm(request.POST)
        if question_form.is_valid():
            question_form.save()
            return HttpResponseRedirect(reverse('add_question'))
        else:
            print "form is invalid"
        print "sdfgfdg"
    
    context = RequestContext(request, {'question_form': question_form})
    return render_to_response('add_question.html', context_instance=context)
    
    
    
