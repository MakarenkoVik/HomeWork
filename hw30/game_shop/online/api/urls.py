from django.urls import path, include

from . import views

urlpatterns = [
    path('games/<str:some_value>', views.GetGameInfoView.as_view()),
]
