from django.urls import path
from visitantes.views import (
    informacoes_visitantes, 
    registrar_visitante, 
    finalizar_visita
)

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('informacoes_visitantes/<int:id>/', informacoes_visitantes, name='informacoes_visitantes'),
    path('registrar_visitante/', registrar_visitante, name='registrar_visitante'),
    path('informacoes_visitantes/<int:id>/finalizar_visita/', finalizar_visita, name='finalizar_visita'),
]
