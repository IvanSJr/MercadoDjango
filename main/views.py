from django.shortcuts import render


def index(request):
    if str(request.user) == 'AnonymousUser':
        usuario = 'Usuário Anônimo'
    else:
        usuario = f'{request.user.first_name} logado'
    context = {
        'curso': 'Programação web com Django-Framework',
        'verifica_logado': usuario
    }
    return render(request, 'index.html', context)


def contato(request):
    return render(request, 'contato.html')
