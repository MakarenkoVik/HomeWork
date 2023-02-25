from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.decorators import api_view
from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer
from store.models import Game, Category
from api.serializers import GameSerializer, CategorySerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import OrderingFilter
from datetime import date


class ResultsSetPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'total'
    max_page_size = 4


class GetGameInfoView(ListAPIView):
    queryset = Game.objects.all()
    renderer_classes = [BrowsableAPIRenderer, JSONRenderer]
    serializer_class = GameSerializer
    pagination_class = ResultsSetPagination
    filter_backends = [OrderingFilter]
    ordering_fields = ['price','game_name','release_date']
