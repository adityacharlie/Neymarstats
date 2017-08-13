from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify as default_slugify

import datetime
import unidecode

class AwayStats(models.Model):
    game_appearences = models.IntegerField(_('game appearences'))
    minutes_played = models.IntegerField(_('minutes played'))
    goals_scored = models.IntegerField(_('goals scored'))
    assists = models.IntegerField(_('assists'))
    yellow_cards = models.IntegerField(_('yellow cards'))
    red_cards = models.IntegerField(_('red cards'))
    shots_per_game = models.DecimalField(_('shots per game'),max_digits=5, decimal_places=2)
    pass_success_percentage = models.DecimalField(_('pass success percentage'),max_digits=5, decimal_places=2)
    aerials_won = models.DecimalField(_('aerials won'),max_digits=5, decimal_places=2)
    man_of_the_match = models.IntegerField(_('man of the match'))
    away_rating = models.DecimalField(_('overall_rating,'),max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode____(self):
        return self.away_rating

class HomeStats(models.Model):
    game_appearences = models.IntegerField(_('game appearences'))
    minutes_played = models.IntegerField(_('minutes played'))
    goals_scored = models.IntegerField(_('goals scored'))
    assists = models.IntegerField(_('assists'))
    yellow_cards = models.IntegerField(_('yellow cards'))
    red_cards = models.IntegerField(_('red cards'))
    shots_per_game = models.DecimalField(_('shots per game'),max_digits=5, decimal_places=2)
    pass_success_percentage = models.DecimalField(_('pass success percentage'),max_digits=5, decimal_places=2)
    aerials_won = models.DecimalField(_('aerials won'),max_digits=5, decimal_places=2)
    man_of_the_match = models.IntegerField(_('man of the match'))
    home_rating = models.DecimalField(_('home rating'),max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    awaystats = models.OneToOneField(
        AwayStats,
        on_delete=models.CASCADE,
        null=True,
    )

    def __unicode____(self):
        return self.home_rating


"""class Stats(models.Model):
    game_appearences = models.IntegerField(_('game appearences'))
    minutes_played = models.IntegerField(_('minutes played'))
    goals_scored = models.IntegerField(_('goals scored'))
    assists = models.IntegerField(_('assists'))
    yellow_cards = models.IntegerField(_('yellow cards'))
    red_cards = models.IntegerField(_('red cards'))
    shots_per_game = models.DecimalField(_('shots per game'),max_digits=5, decimal_places=2)
    pass_success_percentage = models.DecimalField(_('pass success percentage'),max_digits=5, decimal_places=2)
    aerials_won = models.DecimalField(_('aerials won'),max_digits=5, decimal_places=2)
    man_of_the_match = models.IntegerField(_('man of the match'))
    overall_rating = models.DecimalField(_('overall_rating,'),max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    homestats = models.OneToOneField(
        HomeStats,
        on_delete=models.CASCADE,
    )

    def __unicode____(self):
        return self.overall_rating"""


class DefensiveStats(models.Model):
    tackles_per_game = models.DecimalField(_('tackles per game'),max_digits=5, decimal_places=2)
    interceptions_per_game = models.DecimalField(_('interceptions per game'),max_digits=5, decimal_places=2)
    fouls_per_game = models.DecimalField(_('fouls per game'),max_digits=5, decimal_places=2)
    offsides_won_per_game = models.DecimalField(_('offsides won per game'),max_digits=5, decimal_places=2)
    clearances_per_game = models.DecimalField(_('clearances per game'),max_digits=5, decimal_places=2)
    dribbled_past_per_game = models.DecimalField(_('dribbled past per game'),max_digits=5, decimal_places=2)
    outfielder_block_per_game = models.DecimalField(_('outfielder block per game'),max_digits=5, decimal_places=2)
    own_goals = models.IntegerField(_('own goals'),)
    defensive_rating = models.DecimalField(_('defensive rating,'),max_digits=5, decimal_places = 2)
    pub_date = models.DateTimeField(_('date published'), auto_now_add=True)

    def __unicode____(self):
        return self.defensive_rating


class OffensiveStats(models.Model):
    key_passes_per_game = models.DecimalField(_('key passes per game,'),max_digits=5, decimal_places = 2)
    dribbles_per_game = models.DecimalField(_('dribbles per game,'),max_digits=5, decimal_places = 2)
    fouled_per_game = models.DecimalField(_('fouled per game,'),max_digits=5, decimal_places = 2)
    offsides_per_game = models.DecimalField(_('offsides per game,'),max_digits=5, decimal_places = 2)
    dispossessed_per_game = models.DecimalField(_('dispossessed per game,'),max_digits=5, decimal_places = 2)
    badcontrol_per_game = models.DecimalField(_('badcontrol per game,'),max_digits=5, decimal_places = 2)
    offensive_rating = models.DecimalField(_('offensive rating,'),max_digits=5, decimal_places = 2)
    pub_date = models.DateTimeField(_('date published'), auto_now_add=True)    

    def __unicode____(self):
        return self.offensive_rating



class PassingStats(models.Model):
    passes_per_game = models.DecimalField(_('passes per game,'),max_digits=5, decimal_places = 2)
    crosses_per_game = models.DecimalField(_('crosses per game,'),max_digits=5, decimal_places = 2)
    longballs_per_game = models.DecimalField(_('longball per game,'),max_digits=5, decimal_places = 2)
    throughballs_per_game = models.DecimalField(_('throughballs per game,'),max_digits=5, decimal_places = 2)
    passing_rating = models.DecimalField(_('passing rating,'),max_digits=5, decimal_places = 2)
    pub_date = models.DateTimeField(_('date published'), auto_now_add=True)


    def __unicode____(self):
        return self.passing_rating

