from django.shortcuts import render
from main.models import Cliente, Produto
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponse
from django.template import loader
from .forms import ContatoForms, ClienteModelForms, ProdutoModelForms
from django.contrib import messages


def index(request):
    produto = Produto.objects.all()

    if str(request.user) == 'AnonymousUser':
        usuario = 'Anônimo'
    else:
        usuario = f'{str(request.user.first_name)} {str(request.user.last_name)} logado'
    context = {
        'verifica_logado': usuario,
        'produtos': produto
    }
    return render(request, 'index.html', context)


def contato(request):
    if str(request.user) != 'AnonymousUser':
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
    else:
        return redirect('index')


def produto(request, pk):
    # produto_key = Produto.objects.get(id=pk)
    produto_key = get_object_or_404(Produto, id=pk)
    context = {
        'produto': produto_key
    }
    return render(request, 'produto.html', context)


def cadastrocliente(request):
    if str(request.user) != 'AnonymousUser':
        if str(request.method) == 'POST':
            form = ClienteModelForms(request.POST or None)
            if form.is_valid():
                form.save()
                messages.success(request, 'Dados imprimidos com sucesso')
                form = ClienteModelForms()
            else:
                messages.error(request, 'Ocorreu um erro com o formulário')
        else:
            form = ClienteModelForms()
        context = {
            'form': form
        }
        return render(request, 'cadastrocliente.html', context)
    else:
        return redirect('index')


def cadastroproduto(request):
    if str(request.user) != 'AnonymousUser':
        if str(request.method) == 'POST':
            form = ProdutoModelForms(request.POST or None)
            if form.is_valid():
                form.save()
                messages.success(request, 'Dados imprimidos com sucesso')
                form = ProdutoModelForms()
            else:
                messages.error(request, 'Ocorreu um erro com o formulário')
        else:
            form = ProdutoModelForms()
        context = {
            'form': form
        }
        return render(request, 'cadastroproduto.html', context)
    else:
        return redirect('index')


def cliente(request):
    cliente = Cliente.objects.all()
    if str(request.user) == 'AnonymousUser':
        usuario = 'Anônimo'
    else:
        usuario = f'{str(request.user.first_name)} {str(request.user.last_name)} logado'
    context = {
        'verifica_logado': usuario,
        'clientes': cliente
    }
    return render(request, 'cliente.html', context)


def error404(request, exception):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=404)


def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=500)