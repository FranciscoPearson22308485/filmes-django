from django.db.models import Prefetch
from django.shortcuts import render
from .models import Filme, Utilizador, Classificacao


def lista_filmes(request):
    filmes = Filme.objects.prefetch_related('atores')
    return render(request, 'lista_filmes.html', {'filmes': filmes})


def lista_classificacoes(request):
    utilizadores = Utilizador.objects.prefetch_related(
        Prefetch('classificacoes', queryset=Classificacao.objects.select_related('filme'))
    )
    return render(request, 'lista_classificacoes.html', {'utilizadores': utilizadores})
