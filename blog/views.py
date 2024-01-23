from django.shortcuts import render
from .models import Postagem
from .forms import ContatoForm

def pagina_inicio(request):
    ultimas_postagens = Postagem.objects.order_by('-criado_em')[:3]
    return render(request, 'pages/pagina_inicio.html', {'ultimas_postagens': ultimas_postagens})


def pagina_sobre(request):
    return render(request, 'pages/pagina_sobre.html', {})


def pagina_servicos(request):
    return render(request, 'pages/pagina_servicos.html', {})


def pagina_blog(request):
    postagens_basicas = Postagem.objects.filter(premium=False)

    if request.user.is_authenticated and request.user.usuario.premium:
        postagens_premium = Postagem.objects.filter(premium=True)
    else:
        postagens_premium = []

    return render(request, 'pages/pagina_blog.html', {'postagens_basicas': postagens_basicas, 'postagens_premium': postagens_premium})


def pagina_contato(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            # Processar o formulário aqui (por exemplo, enviar e-mail)
            # Neste exemplo, apenas exibimos as informações no console
            print(form.cleaned_data)
    else:
        form = ContatoForm()

    return render(request, 'pages/pagina_contato.html', {'form': form})
