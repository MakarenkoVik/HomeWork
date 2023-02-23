"""online URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.index, name='index'),
    path('categories/', views.all_categories, name='categories'),
    path('category_detail/<slug:slug>', views.category_detail, name='category_detail'),
    path('game_detail/<slug:slug>', views.game, name='game_detail'),
    path('<slug:slug>/comment/', views.CommentCreate.as_view(), name='comment-add'),
    path('comment/<int:pk>/update', views.CommentUpdate.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', views.CommentDelete.as_view(), name='comment-delete'),
]
