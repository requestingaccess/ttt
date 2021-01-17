from django.urls import path

from . import views

urlpatterns = [
    path('games/<int:game_id>', views.games, name='games'),
    path('', views.index, name='index'),
]