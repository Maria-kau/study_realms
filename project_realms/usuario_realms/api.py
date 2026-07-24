from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Profile, Attributes, Progress
from crono_realms.models import StudySession


@login_required
def profile_api(request):
    profile, _ = Profile.objects.get_or_create(user=request.user)
    attributes, _ = Attributes.objects.get_or_create(user=request.user)
    progress_qs = Progress.objects.filter(user=request.user)
    progress_data = [
        {
            "materia": progress.materia,
            "aulas_assistidas": progress.aulas_assistidas,
            "questoes_acertadas": progress.questoes_acertadas,
            "questoes_erradas": progress.questoes_erradas,
            "media_acertos": progress.media_acertos(),
        }
        for progress in progress_qs
    ]

    return JsonResponse({
        "profile": {
            "username": request.user.username,
            "classe": profile.classe,
            "energia": profile.energia,
            "level": profile.level,
            "xp": profile.xp,
            "mana_level": profile.mana_level,
            "mana_xp": profile.mana_xp,
            "aura_level": profile.aura_level,
            "aura_xp": profile.aura_xp,
            "rank": profile.rank,
        },
        "attributes": {
            "inteligencia": attributes.inteligencia,
            "xp_inteligencia": attributes.xp_inteligencia,
            "sabedoria": attributes.sabedoria,
            "xp_sabedoria": attributes.xp_sabedoria,
            "forca": attributes.forca,
            "xp_forca": attributes.xp_forca,
            "destreza": attributes.destreza,
            "xp_destreza": attributes.xp_destreza,
        },
        "progress": progress_data,
    })


@login_required
def study_sessions_api(request):
    sessions = StudySession.objects.filter(user=request.user).order_by("-criada_em")[:20]
    data = [
        {
            "id": session.id,
            "tipo": session.tipo,
            "duracao": session.duracao,
            "concluida": session.concluida,
            "xp_ganho": session.xp_ganho,
            "criada_em": session.criada_em.isoformat(),
        }
        for session in sessions
    ]

    return JsonResponse({
        "study_sessions": data,
    })
