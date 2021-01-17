from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.template import loader

from tttweb.models import Game

def index(request):
    return HttpResponse('Future game index')

def games(request, game_id):
    template = loader.get_template('tttweb/game.html')
    game = get_object_or_404(Game, pk=game_id)
    context = {
        'game': game,
        'ttt': game.ttt,
    }
    return HttpResponse(template.render(context, request))