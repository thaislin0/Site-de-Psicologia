from django.shortcuts import render
from agenda.forms import AgendaForms


def home(request):
    return render(request, 'home.html')


def marcar_consulta(request):
    form = AgendaForms()
    return render(request, 'marcar_consulta.html', {'form': form})


def confirmacao_consulta(request):
    if request.method == 'POST':
        form = AgendaForms(request.POST)
        return render(request, 'confirmacao_consulta.html', {'form': form})


def servicos(request):
    return render(request, 'servicos.html')


def sobre(request):
    return render(request, 'sobre.html')
