from django.db import models
from django.contrib.auth.models import User


class Usuario(models.Model):
    user    = models.OneToOneField(User, on_delete=models.CASCADE)
    premium = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
    

class Categoria(models.Model):
    titulo        = models.CharField(max_length=50)
    descricao     = models.TextField()
    criado_em     = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo


class Postagem(models.Model):
    categoria     = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    titulo        = models.CharField(max_length=200)
    mensagem      = models.TextField()
    premium       = models.BooleanField(default=False)
    criado_em     = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo
