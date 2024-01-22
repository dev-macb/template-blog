from django.shortcuts import render


def pagina_inicio(request):
    return render(request, 'pages/pagina_inicio.html', {})


def pagina_sobre(request):
    return render(request, 'pages/pagina_sobre.html', {})


def pagina_servicos(request):
    return render(request, 'pages/pagina_servicos.html', {})


def pagina_blog(request):
    return render(request, 'pages/pagina_blog.html', {})


def pagina_contato(request):
    return render(request, 'pages/pagina_contato.html', {})
