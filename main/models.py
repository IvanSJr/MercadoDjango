from django.db import models
from django.db.models import signals
from django.template.defaultfilters import slugify

class Base(models.Model):
    criado = models.DateTimeField('Data de Criação', auto_now_add=True)
    modificado = models.DateTimeField('Data de Atualização', auto_now=True)
    ativo = models.BooleanField('Ativado?', default=True)

    class Meta:
        abstract = True


class Produto(Base):
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('Preço', max_digits=10, decimal_places=2)
    estoque = models.IntegerField('Quantidade de Estoque')
    slug = models.SlugField('Slug', max_length=100, editable=False, blank=True)

    def __str__(self):
        return f'{self.nome} {self.estoque}'


def produto_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.nome)


signals.pre_save.connect(produto_pre_save, sender=Produto)


class Cliente(Base):
    nome = models.CharField('Nome', max_length=100)
    sobrenome = models.CharField('Sobrenome', max_length=100)
    email = models.EmailField('E-mail', max_length=100)
    slug = models.SlugField('Slug', max_length=100, editable=False, blank=True)

    def __str__(self):
        return f'{self.nome.title()} {self.sobrenome.title()}'


def cliente_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.nome)


signals.pre_save.connect(cliente_pre_save, sender=Cliente)
