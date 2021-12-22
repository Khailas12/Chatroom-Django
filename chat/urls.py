from django.urls import path
from . import views


urlpatters = [
    path('', views.index, name='index'),
    path('<str:room_name/', views.room, name='room'),   # to access chatroom
]