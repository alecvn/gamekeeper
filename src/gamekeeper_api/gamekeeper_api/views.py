from rest_framework import routers, serializers, viewsets
from rest_framework import response

from gamekeeper.models import Player, Event

class PlayerSerializer(serializers.ModelSerializer):
     total_points = serializers.SerializerMethodField('total_points')

     def total_points(self, obj):
         return obj.total_points(data['event'])
    
     class Meta:
         model = Player
         fields = ('full_name', 'event',)#'total_points')
         extra_kwargs = {'event': None}

class PlayerViewSet(viewsets.ViewSet):
    queryset = Player.objects.all()
#    serializer_class = PlayerSerializer
    
    def list(self, request, event_pk=None):
        queryset = Event.objects.get(pk=event_pk).players
        serializer = PlayerSerializer(queryset, many=True, data={'event':Event.objects.get(pk=event_pk)})
        serializer.is_valid()
        return response.Response(serializer.initial_data)


    # def retrieve(self, request, pk=None, event_pk=None):
    #     nameservers = self.queryset.get(pk=pk, domain=domain_pk)
    #     (...)
    #     return Response(serializer.data)
