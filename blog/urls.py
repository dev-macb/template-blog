from . import views
from django.urls import path
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.pagina_inicio, name='pagina_inicio'),
    path('sobre/', views.pagina_sobre, name='pagina_sobre'),
    path('servicos/', views.pagina_servicos, name='pagina_servicos'),
    path('blog/', views.pagina_blog, name='pagina_blog'),
    path('blog/<int:id_postagem>', views.pagina_visualizar_postagem, name='pagina_visualizar_postagem'),
    path('contato/', views.pagina_contato, name='pagina_contato'),

    path('entrar/', views.pagina_entrar, name='pagina_entrar'),
    path('registrar-se/', views.pagina_registrar_se, name='pagina_registrar_se'),
]
