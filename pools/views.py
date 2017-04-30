from .forms import QuestionForm, NeyStatsForm, NeyHomeStatsForm
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import *
from django.shortcuts import render, render_to_response, get_object_or_404


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
    

def question_list(request):
    questions = Question.objects.all()
    
    context = RequestContext(request, {'questions': questions})
    return render_to_response('question_list.html', context_instance=context)


def add_ney_stats(request, sid=None):
    if sid:
        stat = get_object_or_404(Stats, pk=sid)
    else:
        stat = Stats()
    ney_stats_form = NeyStatsForm()
    if request.method == 'POST':
        ney_stats_form = NeyStatsForm(request.POST,instance=stat)
        if ney_stats_form.is_valid():
            ney_stats_form.save()
            return HttpResponseRedirect(reverse('ney_stat_list'))
        else:
            print "form is invalid"
    else:
        ney_stats_form = NeyStatsForm(instance=stat)
    context = RequestContext(request, {'ney_stats_form': ney_stats_form})
    #return render_to_response('add_ney_stats.html', context_instance=context)
    return render(request, 'add_ney_stats.html', {'context': context})


def add_ney_home_stats(request):
    ney_home_stats_form = NeyHomeStatsForm()
    if request.method == 'POST':
        ney_home_stats_form = NeyHomeStatsForm(request.POST)
        if ney_home_stats_form.is_valid():
            ney_home_stats_form.save()
            return HttpResponseRedirect(reverse('add_ney_home_stats'))
        else:
            print "form is invalid"
    context = RequestContext(request, {'ney_home_stats_form': ney_home_stats_form})
    return render(request, 'add_ney_home_stats.html', {'context': context})


def ney_stat_list(request):
    return render (request, 'ney_stats_list.html', {'stats': Stats.objects.all() })    






