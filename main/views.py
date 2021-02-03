from django.shortcuts import render
from main.models import Cliente, Produto


def index(request):
    produto = Produto.objects.all()

    if str(request.user) == 'AnonymousUser':
        usuario = 'Usuário Anônimo'
    else:
        usuario = f'{request.user.first_name} Logado'
    context = {
        'curso': 'Programação web com Django-Framework',
        'verifica_logado': usuario,
        'produtos': produto
    }
    return render(request, 'index.html', context)


def contato(request):
    return render(request, 'contato.html')


def produto(request, pk):
    produto_key = Produto.objects.get(id=pk)
    context = {
        'produto': produto_key
    }
    return render(request, 'produto.html', context)
