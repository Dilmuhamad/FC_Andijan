from django.urls import path
from .views import *
from django.urls import include


urlpatterns = [
    path('get_new_slider/', get_new_slider),
    path('get_video/', get_video),
    path('get_players/', get_player),
    path('get_shop/', get_shop),
    path('get_arenas_information/', get_arenas_information),
    path('get_partners/', get_partner),
    path('get_news/', get_new),
    path('get_club/', get_club),
    path('get_arena/', get_arena),
    path('get_academy/', get_academy),
    path('delete-players/<int:pk>/', delete_player_view),
]


