from django.shortcuts import render
from main.models import Cliente, Produto
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .forms import ContatoForms
from django.contrib import messages


def index(request):
    produto = Produto.objects.all()

    if str(request.user) == 'AnonymousUser':
        usuario = 'Anônimo'
    else:
        usuario = f'{str(request.user.first_name)} {str(request.user.last_name)} logado'
    context = {
        'curso': 'Programação web com Django-Framework',
        'verifica_logado': usuario,
        'produtos': produto
    }
    return render(request, 'index.html', context)


def contato(request):
    form = ContatoForms(request.POST or None)

    if str(request.method) == "POST":
        if form.is_valid():
            form.enviar_email()
            messages.success(request, 'E-mail enviado com sucesso')
            form = ContatoForms()
        else:
            messages.error(request, 'Ocorreu um erro ao enviar o e-mail')

    context = {
        'form': form
    }
    return render(request, 'contato.html', context)


def produto(request, pk):
    # produto_key = Produto.objects.get(id=pk)
    produto_key = get_object_or_404(Produto, id=pk)
    context = {
        'produto': produto_key
    }
    return render(request, 'produto.html', context)


def error404(request, exception):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=404)


def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=500)