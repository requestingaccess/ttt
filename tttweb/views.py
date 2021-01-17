from django.http import HttpResponse

from tttweb.tictactoe import TicTacToe

def index(request):
    game = TicTacToe()
    return HttpResponse('The board: {}'.format(game.board))
