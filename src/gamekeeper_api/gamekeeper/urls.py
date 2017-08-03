from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^games/index/$', views.list_games, name='list_games'),
    url(r'^games/create/$', views.create_game, name='create_game'),
    url(r'^rules/index/$', views.list_rules, name='list_rules'),
    url(r'^rules/create/$', views.create_rule, name='create_rule'),
    url(r'^players/index/$', views.list_players, name='list_players'),
    url(r'^players/create/$', views.create_player, name='create_player'),
    # url(r'^matches/index/$', views.list_matches, name='list_matches'),
    # url(r'^matches/create/$', views.create_match, name='create_match'),
    url(r'^games/(?P<game_id>[0-9]+)/events/index/$', views.list_events, name='list_events'),
    url(r'^games/(?P<game_id>[0-9]+)/events/create/$', views.create_event, name='create_event'),
    url(r'^games/(?P<game_id>[0-9]+)/events/(?P<event_id>[0-9]+)/show/$', views.show_event, name='show_events'),
]
