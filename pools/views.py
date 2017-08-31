from .forms import NeyAwayStatsForm, NeyHomeStatsForm
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import AwayStats, HomeStats
from django.shortcuts import render, render_to_response, get_object_or_404


# Create your views here.


def add_ney_stats(request, sid=None):
    if sid:
        homestats = get_object_or_404(HomeStats, pk=sid)
        awaystats = get_object_or_404(AwayStats, pk=homestats.awaystats_id)
    else:
        homestats = HomeStats()
        awaystats = AwayStats()
    ney_home_stats_form = NeyHomeStatsForm()
    ney_away_stats_form = NeyAwayStatsForm()

    if request.method == 'POST' and 'away_submit' in request.POST:
        ney_away_stats_form = NeyAwayStatsForm(request.POST,instance=awaystats)
        print ney_away_stats_form
        if ney_away_stats_form.is_valid():
            ney_away_stats_form.save()
            return HttpResponseRedirect(reverse('ney_stat_list'))
        else:
            print ney_away_stats_form.errors
    else:
        ney_away_stats_form = NeyAwayStatsForm(instance=awaystats)
        
    if request.method == 'POST' and 'home_submit' in request.POST:
        ney_home_stats_form = NeyHomeStatsForm(request.POST,instance=homestats)
        print ney_home_stats_form
        if ney_home_stats_form.is_valid():
            ney_home_stats_form.save()
            return HttpResponseRedirect(reverse('ney_stat_list'))
        else:
            print "form is invalid"
            print ney_home_stats_form.errors
    else:
        ney_home_stats_form = NeyHomeStatsForm(instance=homestats)

    

    context = RequestContext(request, {'ney_home_stats_form': ney_home_stats_form,
                                       'ney_away_stats_form': ney_away_stats_form})
    
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






