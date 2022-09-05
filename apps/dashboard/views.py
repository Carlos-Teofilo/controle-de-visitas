from django.shortcuts import render

from visitantes.models import Visitante


def index(request):

    todos_visitantes = Visitante.objects.all()

    context = {
        'nome_pagina': 'Início da dashboard',
        'todos_visitantes': todos_visitantes,
        'visitantes_aguardando': Visitante.objects.filter(status='AGUARDANDO').count(),
        'visitantes_em_visita': Visitante.objects.filter(status__startswith='EM_').count(),
        'visitantes_finalizados': Visitante.objects.filter(status__startswith='FIN').count(),
    }
    return render(request, 'index.html', context)
