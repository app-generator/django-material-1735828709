# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Team(models.Model):

    #__Team_FIELDS__
    name = models.TextField(max_length=255, null=True, blank=True)

    #__Team_FIELDS__END

    class Meta:
        verbose_name        = _("Team")
        verbose_name_plural = _("Team")


class Player(models.Model):

    #__Player_FIELDS__
    teamid = models.ForeignKey(Team, on_delete=models.CASCADE)
    name = models.TextField(max_length=255, null=True, blank=True)

    #__Player_FIELDS__END

    class Meta:
        verbose_name        = _("Player")
        verbose_name_plural = _("Player")


class Tournamenttype(models.Model):

    #__Tournamenttype_FIELDS__
    setsorlegs = models.IntegerField(null=True, blank=True)
    bestofnumber = models.IntegerField(null=True, blank=True)
    points = models.IntegerField(null=True, blank=True)
    format = models.TextField(max_length=255, null=True, blank=True)

    #__Tournamenttype_FIELDS__END

    class Meta:
        verbose_name        = _("Tournamenttype")
        verbose_name_plural = _("Tournamenttype")


class Tournament(models.Model):

    #__Tournament_FIELDS__
    name = models.TextField(max_length=255, null=True, blank=True)
    tournamenttypeid = models.ForeignKey(TournamentType, on_delete=models.CASCADE)
    startdate = models.DateTimeField(blank=True, null=True, default=timezone.now)
    enddate = models.DateTimeField(blank=True, null=True, default=timezone.now)
    numberofrounds = models.IntegerField(null=True, blank=True)

    #__Tournament_FIELDS__END

    class Meta:
        verbose_name        = _("Tournament")
        verbose_name_plural = _("Tournament")


class Board(models.Model):

    #__Board_FIELDS__
    name = models.TextField(max_length=255, null=True, blank=True)

    #__Board_FIELDS__END

    class Meta:
        verbose_name        = _("Board")
        verbose_name_plural = _("Board")


class Game(models.Model):

    #__Game_FIELDS__
    tournamentid = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    boardid = models.ForeignKey(Board, on_delete=models.CASCADE)
    gamedate = models.DateTimeField(blank=True, null=True, default=timezone.now)
    hometeamid = models.ForeignKey(Team, on_delete=models.CASCADE)
    awayteamid = models.ForeignKey(Team, on_delete=models.CASCADE)
    callerid = models.ForeignKey(Player, on_delete=models.CASCADE)
    roundnumber = models.IntegerField(null=True, blank=True)
    playoffid = models.ForeignKey(Playoff, on_delete=models.CASCADE)

    #__Game_FIELDS__END

    class Meta:
        verbose_name        = _("Game")
        verbose_name_plural = _("Game")


class Result(models.Model):

    #__Result_FIELDS__
    gameid = models.ForeignKey(Game, on_delete=models.CASCADE)
    homesets = models.IntegerField(null=True, blank=True)
    awaysets = models.IntegerField(null=True, blank=True)
    homelegs = models.IntegerField(null=True, blank=True)
    awaylegs = models.IntegerField(null=True, blank=True)

    #__Result_FIELDS__END

    class Meta:
        verbose_name        = _("Result")
        verbose_name_plural = _("Result")


class Gamestatistics(models.Model):

    #__Gamestatistics_FIELDS__
    gameid = models.ForeignKey(Game, on_delete=models.CASCADE)
    teamid = models.ForeignKey(Team, on_delete=models.CASCADE)
    playerid = models.ForeignKey(Player, on_delete=models.CASCADE)
    setswon = models.IntegerField(null=True, blank=True)
    setslost = models.IntegerField(null=True, blank=True)
    legswon = models.IntegerField(null=True, blank=True)
    legslost = models.IntegerField(null=True, blank=True)
    average = models.IntegerField(null=True, blank=True)
    highestcheckout = models.IntegerField(null=True, blank=True)
    checkout = models.IntegerField(null=True, blank=True)
    status = models.TextField(max_length=255, null=True, blank=True)

    #__Gamestatistics_FIELDS__END

    class Meta:
        verbose_name        = _("Gamestatistics")
        verbose_name_plural = _("Gamestatistics")


class Playoff(models.Model):

    #__Playoff_FIELDS__
    name = models.TextField(max_length=255, null=True, blank=True)
    trounamentid = models.ForeignKey(Tournament, on_delete=models.CASCADE)

    #__Playoff_FIELDS__END

    class Meta:
        verbose_name        = _("Playoff")
        verbose_name_plural = _("Playoff")



#__MODELS__END
