from django.urls import path
from .views import index, contato, cadastroproduto, produto, cadastrocliente, cliente


urlpatterns = [
    path('', index, name='index'),
    path('contato', contato, name='contato'),
    path('cadastroprodutos', cadastroproduto, name='cadastroproduto'),
    path('produto/<int:pk>', produto, name='produto'),
    path('cadastroclientes', cadastrocliente, name='cadastrocliente'),
    path('cliente', cliente, name='cliente'),
]