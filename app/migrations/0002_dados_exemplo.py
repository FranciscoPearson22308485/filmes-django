from django.db import migrations


def criar_dados_exemplo(apps, schema_editor):
    Ator = apps.get_model('app', 'Ator')
    Filme = apps.get_model('app', 'Filme')
    Utilizador = apps.get_model('app', 'Utilizador')
    Classificacao = apps.get_model('app', 'Classificacao')

    if Filme.objects.exists():
        return

    viggo = Ator.objects.create(nome='Viggo Mortensen')
    cate = Ator.objects.create(nome='Cate Blanchett')
    robert = Ator.objects.create(nome='Robert De Niro')
    joe = Ator.objects.create(nome='Joe Pesci')
    maria = Ator.objects.create(nome='Maria de Medeiros')

    anel = Filme.objects.create(
        titulo='O Senhor dos Anéis: O Regresso do Rei',
        data_lancamento='2003-12-17',
        pais_origem='Nova Zelândia',
    )
    anel.atores.add(viggo, cate)

    irishman = Filme.objects.create(
        titulo='The Irishman',
        data_lancamento='2019-11-27',
        pais_origem='Estados Unidos',
    )
    irishman.atores.add(robert, joe)

    capitães = Filme.objects.create(
        titulo='Capitães de Abril',
        data_lancamento='2000-04-21',
        pais_origem='Portugal',
    )
    capitães.atores.add(maria)

    ana = Utilizador.objects.create(nome='Ana Martins')
    rui = Utilizador.objects.create(nome='Rui Silva')

    Classificacao.objects.create(utilizador=ana, filme=anel, nota=5)
    Classificacao.objects.create(utilizador=ana, filme=capitães, nota=4)
    Classificacao.objects.create(utilizador=rui, filme=irishman, nota=5)


def remover_dados_exemplo(apps, schema_editor):
    Ator = apps.get_model('app', 'Ator')
    Filme = apps.get_model('app', 'Filme')
    Utilizador = apps.get_model('app', 'Utilizador')
    Classificacao = apps.get_model('app', 'Classificacao')

    titulos = [
        'O Senhor dos Anéis: O Regresso do Rei',
        'The Irishman',
        'Capitães de Abril',
    ]
    nomes_atores = [
        'Viggo Mortensen',
        'Cate Blanchett',
        'Robert De Niro',
        'Joe Pesci',
        'Maria de Medeiros',
    ]
    nomes_utilizadores = ['Ana Martins', 'Rui Silva']

    Classificacao.objects.filter(filme__titulo__in=titulos, utilizador__nome__in=nomes_utilizadores).delete()
    Filme.objects.filter(titulo__in=titulos).delete()
    Utilizador.objects.filter(nome__in=nomes_utilizadores).delete()
    Ator.objects.filter(nome__in=nomes_atores).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(criar_dados_exemplo, remover_dados_exemplo),
    ]
