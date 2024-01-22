from django.shortcuts import render
from .models import Postagem


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
    return render(request, 'pages/pagina_contato.html', {})
