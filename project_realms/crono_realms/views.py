from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    return render(request, "crono_realms/home.html")


@login_required
def configuracao(request):
    return render(request, "crono_realms/configuracao.html")


@login_required
def progresso(request):
    return render(request, "crono_realms/progresso.html")