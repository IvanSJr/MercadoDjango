from django import forms
from django.core.mail.message import EmailMessage
from .models import Cliente, Produto


class ContatoForms(forms.Form):
    nome = forms.CharField(label='Digite seu nome', max_length=100, min_length=1, required=True)
    email = forms.EmailField(label='Digite seu email', max_length=100, required=True)
    assunto = forms.CharField(label='Digite o assunto do email', max_length=100)
    mensagem = forms.CharField(label='Digite aqui a sua mensagem', widget=forms.Textarea())

    def enviar_email(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['mensagem']

        conteudo = f'Nome: {nome}\n Email: {email}\n Assunto: {assunto}\n Mensagem: {mensagem}'

        mail = EmailMessage(
            subject=assunto,
            body= conteudo,
            from_email='contato@django.naavii.com.br',
            to=[email],
            headers={'Reply-to': email}
        )
        mail.send()


class ClienteModelForms(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'sobrenome', 'email']


class ProdutoModelForms(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'preco', 'estoque']
