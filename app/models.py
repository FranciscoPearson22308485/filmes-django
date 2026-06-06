from django.db import models

class Ator(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Filme(models.Model):
    titulo = models.CharField(max_length=200)
    data_lancamento = models.DateField()
    pais_origem = models.CharField(max_length=100)
    atores = models.ManyToManyField(Ator, related_name='filmes')

    def __str__(self):
        return self.titulo

class Utilizador(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Classificacao(models.Model):
    utilizador = models.ForeignKey(
        Utilizador, on_delete=models.CASCADE, related_name='classificacoes'
    )
    filme = models.ForeignKey(
        Filme, on_delete=models.CASCADE, related_name='classificacoes'
    )
    nota = models.IntegerField()

    def __str__(self):
        return f'{self.utilizador.nome} -> {self.filme.titulo}: {self.nota}'
