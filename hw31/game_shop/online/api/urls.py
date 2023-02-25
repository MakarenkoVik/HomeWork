from django.urls import path

from . import views

urlpatterns = [
    path('games/', views.GetGameInfoView.as_view()),
]
