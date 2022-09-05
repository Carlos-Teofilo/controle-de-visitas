from django.shortcuts import render
from django.utils import timezone

from visitantes.models import Visitante


def index(request):

    todos_visitantes = Visitante.objects.order_by('-horario_chegada')


    mes_atual = timezone.now().month

    context = {
        'nome_pagina': 'Início da dashboard',
        'todos_visitantes': todos_visitantes,
        'visitantes_aguardando': Visitante.objects.filter(status='AGUARDANDO').count(),
        'visitantes_em_visita': Visitante.objects.filter(status__startswith='EM_').count(),
        'visitantes_finalizados': Visitante.objects.filter(status__startswith='FIN').count(),
        'visitantes_mensal': Visitante.objects.filter(
            horario_chegada__month=mes_atual
            ).count()
    }
    return render(request, 'index.html', context)
