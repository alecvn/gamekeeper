from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^index/$', views.list_games, name='list_games'),
    url(r'^create/$', views.create_game, name='create_game'),
]
