from django import forms


class ContatoForm(forms.Form):
    assuntos = [
        ('geral', 'Geral'),
        ('suporte', 'Suporte'),
        ('feedback', 'Feedback'),
    ]

    nome = forms.CharField(max_length=100)
    telefone = forms.CharField(max_length=20)
    email = forms.EmailField()
    assunto = forms.ChoiceField(choices=assuntos)
    mensagem = forms.CharField(widget=forms.Textarea)
    