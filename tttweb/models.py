import json
from tttweb.tictactoe import TicTacToe

from django.contrib.auth.models import User
from django.db import models


class Game(models.Model):
    created = models.DateTimeField('date created')
    updated = models.DateTimeField('date updated')

    name = models.CharField(max_length=200, null=False, blank=False)

    player0 = models.ForeignKey(User, models.SET_NULL, null=True, related_name='player0')
    player1 = models.ForeignKey(User, models.SET_NULL, null=True, related_name='player1')

    board_text = models.CharField(max_length=200)
    player = models.IntegerField(default=0)

    @property
    def ttt(self):
        return TicTacToe.from_game(self)