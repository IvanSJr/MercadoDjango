from django.urls import path
from .views import index, contato, produto, cadastro, cliente


urlpatterns = [
    path('', index, name='index'),
    path('contato', contato, name='contato'),
    path('produto/<int:pk>', produto, name='produto'),
    path('cadastro', cadastro, name='cadastro'),
    path('cliente', cliente, name='cliente'),
]