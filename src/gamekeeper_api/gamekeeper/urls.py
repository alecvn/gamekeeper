from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^games/index/$', views.list_games, name='list_games'),
    url(r'^games/create/$', views.create_game, name='create_game'),
    url(r'^rules/index/$', views.list_rules, name='list_rules'),
    url(r'^rules/create/$', views.create_rule, name='create_rule'),
    url(r'^rules/(?P<rule_id>[0-9]+)/show/$', views.show_rule, name='show_rule'),
    url(r'^rules/(?P<rule_id>[0-9]+)/update/$', views.update_rule, name='update_rule'),
    url(r'^players/index/$', views.list_players, name='list_players'),
    url(r'^players/create/$', views.create_player, name='create_player'),
    url(r'^actions/index/$', views.list_actions, name='list_actions'),
    url(r'^actions/create/$', views.create_action, name='create_action'),
    url(r'^actions/evaluate/$', views.evaluate_actions, name='evaluate_actions'),
    url(r'^points/index/$', views.list_points, name='list_points'),
    url(r'^points/create/$', views.create_point, name='create_point'),
    url(r'^games/(?P<game_id>[0-9]+)/events/(?P<event_id>[0-9]+)/results/index/$', views.list_results, name='list_results'),
    url(r'^games/(?P<game_id>[0-9]+)/events/(?P<event_id>[0-9]+)/results/evaluate_actions/$', views.evaluate_actions, name='evaluate_actions'),
    url(r'^games/(?P<game_id>[0-9]+)/events/index/$', views.list_events, name='list_events'),
    url(r'^games/(?P<game_id>[0-9]+)/events/create/$', views.create_event, name='create_event'),
    url(r'^games/(?P<game_id>[0-9]+)/events/(?P<event_id>[0-9]+)/update/$', views.update_event, name='update_event'),
    url(r'^games/(?P<game_id>[0-9]+)/events/(?P<event_id>[0-9]+)/show/$', views.show_event, name='show_event'),
]
