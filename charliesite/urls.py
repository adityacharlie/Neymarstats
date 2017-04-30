"""charliesite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
import pools.views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^question/add/$', pools.views.add_question, name='add_question'),
    url(r'^question/list/$', pools.views.question_list, name='question_list'),


    # Stats URLs
    url(r'^ney/stats/$', pools.views.add_ney_stats, name='add_ney_stats'),
    url(r'^ney/stats/(?P<sid>\d+)/$', pools.views.add_ney_stats, name='edit_ney_stats'),
    url(r'^ney/stats/list/$', pools.views.ney_stat_list, name = 'ney_stat_list'),


    url(r'ney/homestats/add/$', pools.views.add_ney_home_stats, name='add_ney_home_stats'),
    #url(r'ney/awaystats/add/$', pools.views.add_ney_away_stats, name='add_ney_away_stats'),
    #url(r'ney/defensivestats/add/$', pools.views.add_ney_defensive_stats, name='add_ney_defensive_stats'),
    #url(r'ney/offensivestats/add/$', pools.views.add_ney_offensive_stats, name='add_ney_offensive_stats'),
    #url(r'ney/passingstats/add/$', pools.views.add_ney_passing_stats, name='add_ney_passing_stats'),

]




