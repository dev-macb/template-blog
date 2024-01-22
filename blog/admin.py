from django.contrib import admin
from .models import Categoria, Postagem, Usuario


admin.site.register(Usuario)
admin.site.register(Categoria)
admin.site.register(Postagem)
