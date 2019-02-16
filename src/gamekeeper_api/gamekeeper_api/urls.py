"""particirate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url, include

from django.contrib.auth.models import User
from django.contrib import admin
from rest_framework.decorators import api_view
from rest_framework import routers, serializers, viewsets
#from rest_framework_nested import routers

from gamekeeper.models import Player, Event, Point, ActionResult, Rule, Action
from gamekeeper import views


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PointSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Point
        fields = ('description', 'allocation',)

class PointViewSet(viewsets.ModelViewSet):
    queryset = Point.objects.all()
    serializer_class = PointSerializer

class PlayerSerializer(serializers.ModelSerializer):
     # total_points = serializers.SerializerMethodField('total_points')

     # def total_points(self, obj):
     #     return obj.total_points()
    
     class Meta:
         model = Player
         fields = ('id', 'full_name', )#'total_points')
        
class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

class RuleSerializer(serializers.HyperlinkedModelSerializer):
     class Meta:
         model = Rule
         fields = ('id', 'description')
        
class RuleViewSet(viewsets.ModelViewSet):
    queryset = Rule.objects.all()
    serializer_class = RuleSerializer

class ActionSerializer(serializers.HyperlinkedModelSerializer):
     class Meta:
         model = Action
         fields = ('id', 'description')
        
class ActionViewSet(viewsets.ModelViewSet):
    queryset = Action.objects.all()
    serializer_class = ActionSerializer

class ActionResultSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ActionResult
        fields = ('description', 'event_id', 'action_id', 'player_id',)

class ActionResultViewSet(viewsets.ModelViewSet):
    queryset = ActionResult.objects.all()
    serializer_class = ActionResultSerializer


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
#router = routers.SimpleRouter()
router.register(r'events', views.EventViewSet)
router.register(r'users', UserViewSet)
router.register(r'players', PlayerViewSet)

# events_router = routers.NestedSimpleRouter(router, r'events', lookup='event')
# events_router.register(r'players', PlayerViewSet, base_name='event-players')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
#    url(r'^', include(events_router.urls)),
    # url(r'^events/(?P<event_id>[0-9]+)/players/(?P<player_id>[0-9]+)/details/$', views.player_event_context),
    url(r'^events/(?P<event_id>[0-9]+)/players/$', views.player_event_context),
    url(r'^action_results/$', views.action_result_list),
    url(r'^clone_event/$', views.clone_event),
    url(r'^admin/', admin.site.urls),
    url(r'^', include('gamekeeper.urls')),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
