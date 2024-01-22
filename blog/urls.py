from . import views
from django.urls import path


urlpatterns = [
    path('', views.pagina_inicio, name='pagina_inicio'),
    path('sobre/', views.pagina_sobre, name='pagina_sobre'),
    path('servicos/', views.pagina_servicos, name='pagina_servicos'),
    path('blog/', views.pagina_blog, name='pagina_blog'),
    path('contato/', views.pagina_contato, name='pagina_contato')
]
