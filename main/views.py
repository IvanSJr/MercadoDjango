from django.shortcuts import render
from main.models import Cliente, Produto


def index(request):
    produto = Produto.objects.all()

    if str(request.user) == 'AnonymousUser':
        usuario = 'Usuário Anônimo'
    else:
        usuario = f'{request.user.first_name} logado'
    context = {
        'curso': 'Programação web com Django-Framework',
        'verifica_logado': usuario,
        'produtos': produto
    }
    return render(request, 'index.html', context)


def contato(request):
    return render(request, 'contato.html')
