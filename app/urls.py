from django.urls import path
from . import views

urlpatterns = [
    path('filmes/', views.lista_filmes, name='lista_filmes'),
    path('classificacoes/', views.lista_classificacoes, name='lista_classificacoes'),
]
