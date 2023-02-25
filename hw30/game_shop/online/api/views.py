from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer
from store.models import Game, Category
from api.serializers import GameSerializer, CategorySerializer


class GetGameInfoView(APIView):

    renderer_classes = [BrowsableAPIRenderer, JSONRenderer]

    def get(self, request, some_value):
        queryset = Game.objects.all()
        serializer_for_queryset = GameSerializer(instance=queryset, many=True)
        return Response({"games": serializer_for_queryset.data})
