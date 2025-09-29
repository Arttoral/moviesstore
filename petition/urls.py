from django.urls import path
from . import views

app_name = 'petition'

urlpatterns = [
    path('', views.petition_list, name='list'),
    path('create/', views.create_petition, name='create'),
    path('vote/<int:petition_id>/', views.vote_petition, name='vote'),
]
