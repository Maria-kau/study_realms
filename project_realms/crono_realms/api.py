from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import StudySession


@login_required
def study_history_api(request):
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
        "study_history": data,
    })
