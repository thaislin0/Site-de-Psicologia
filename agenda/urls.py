from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('confirmacao_consulta', views.home, name='confirmacao_consulta'),
    path('marcar_consulta', views.marcar_consulta, name='marcar_consulta'),
    path('confirmacao_consulta', views.confirmacao_consulta, name='confirmacao_consulta'),
    path('servicos', views.servicos, name='servicos'),
    path('sobre', views.sobre, name='sobre'),
]
