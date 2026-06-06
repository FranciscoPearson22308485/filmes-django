# Filmes Django — Exercício 12

## Modelos

- Ator, Filme (N:M com Ator), Utilizador, Classificacao (FK Utilizador + FK Filme + nota)

## Vistas

- `/filmes/` — lista filmes com atores
- `/classificacoes/` — lista utilizadores com as suas classificações

## Setup

```bash
python manage.py migrate && python manage.py createsuperuser && python manage.py runserver
```

**Autor:** Francisco Pearson — 22308485 | Universidade Lusófona · PW 2025/26
