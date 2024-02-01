from django.shortcuts import render, get_object_or_404
from .models import Postagem, Categoria
from .forms import ContatoForm

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

def pagina_inicio(request):
    numero_categorias = Categoria.objects.count()
    numero_postagens = Postagem.objects.count()

    if request.user.is_authenticated and request.user.usuario.premium:
        postagens_recentes = Postagem.objects.order_by('-criado_em')[:4]
    else:
        postagens_recentes = Postagem.objects.filter(premium=False).order_by('-criado_em')[:4]

    return render(request, 'pages/inicio.html', {
        'ultima_postagem': postagens_recentes[0],
        'postagens_recentes': postagens_recentes, 
        'numero_categorias': numero_categorias, 
        'numero_postagens': numero_postagens
    })


def pagina_sobre(request):
    return render(request, 'pages/pagina_sobre.html', {})


def pagina_servicos(request):
    return render(request, 'pages/pagina_servicos.html', {})


def pagina_blog(request):
    query = request.GET.get('filtro', '')
 
    if request.user.is_authenticated and request.user.usuario.premium:
        postagens = Postagem.objects.filter(titulo__icontains=query).order_by('-criado_em')
    else:
        postagens = Postagem.objects.filter(titulo__icontains=query, premium=False).order_by('-criado_em')

    return render(request, 'pages/blog.html', {
        'postagens': postagens, 
        'numero_postagens': len(postagens)
    })


def pagina_visualizar_postagem(request, id_postagem):
    postagem = get_object_or_404(Postagem, id=id_postagem)

    return render(request, 'pages/pagina_visualizar_postagem.html', {
        'postagem': postagem
    })


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


def pagina_entrar(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('inicio')
    else:
        form = AuthenticationForm()

    return render(request, 'pages/entrar.html', {'form': form})


def pagina_registrar_se(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('pagina_inicio')
    else:
        form = UserCreationForm()

    return render(request, 'pages/registrar_se.html', {'form': form})