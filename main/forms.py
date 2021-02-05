from django import forms


class ContatoForms(forms.Form):
    nome = forms.CharField(label='Digite seu nome', max_length=100, min_length=1, required=True)
    email = forms.EmailField(label='Digite seu email', max_length=100, required=True)
    assunto = forms.CharField(label='Digite o assunto do email', max_length=100)
    mensagem = forms.CharField(label='Digite aqui a sua mensagem', widget=forms.Textarea())


