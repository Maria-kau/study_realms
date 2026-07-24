from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import StudySession
from .services.study import register_study
from .services.realms import get_realm
from .services.reset import reset_weekly_realm


# =====================================
# HOME
# =====================================
@login_required
def home(request):
    return render(
        request,
        "crono_realms/home.html"
    )


# =====================================
# CONFIGURAÇÃO
# =====================================
@login_required
def configuracao(request):
    return render(
        request,
        "crono_realms/configuracao.html"
    )


# =====================================
# DESENVOLVIMENTO
# =====================================
@login_required
def desenvolvimento(request):
    return render(
        request,
        "crono_realms/desenvolvimento.html"
    )


# =====================================
# REINO
# =====================================
@login_required
def reino_view(request):
    # Obtém o reino do usuário e verifica o reset semanal
    realm = get_realm(request.user)
    reset_weekly_realm(realm)

    # Coleta todas as construções vinculadas ao reino do usuário
    buildings = realm.buildings.select_related("tile")

    return render(
        request,
        "crono_realms/timer.html",  # Mantido para o seu template de mapa centralizado
        {
            "construcoes": buildings
        }
    )


# =====================================
# TIMER
# =====================================
@login_required
def timer_view(request):
    # Obtém o reino do usuário e verifica o reset semanal
    realm = get_realm(request.user)
    reset_weekly_realm(realm)

    # Carrega as construções para que o mapa de fundo não inicie vazio no Temporizador
    buildings = realm.buildings.select_related("tile")

    return render(
        request,
        "crono_realms/timer.html",
        {
            "tipos": StudySession.TIPO_CHOICES,
            "construcoes": buildings,
            "realm": realm,  # Envia o reino com os contadores para o HTML
        }
    )


# =====================================
# FINALIZAR ESTUDO
# =====================================
@login_required
def complete_study(request):
    if request.method != "POST":
        return redirect("timer")

    tipo = request.POST.get("tipo")

    try:
        duracao = int(request.POST.get("duracao", 0))
    except ValueError:
        duracao = 0

    concluida = (request.POST.get("concluida", "nao") == "sim")

    # CORRIGIDO AQUI: Agora desempacota o XP e o Total de Construções retornados pelo service
    xp_ganho, total_construcoes = register_study(
        user=request.user,
        tipo=tipo,
        duracao=duracao,
        concluida=concluida
    )

    # Deixa a mensagem dinâmica e mais legal para o usuário!
    if total_construcoes > 0:
        msg = f"Sessão concluída! +{xp_ganho} XP e +{total_construcoes} estrutura(s) adicionada(s) ao seu Reino! 🌳"
    else:
        msg = f"Sessão registrada! +{xp_ganho} XP."

    messages.success(request, msg)

    return redirect("timer")

