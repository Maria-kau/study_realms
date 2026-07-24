from usuario_realms.models import Avatar


def avatars_available(profile):
    genero_personagem = (getattr(profile, "genero_personagem", "") or "").strip() or "masculino"

    return Avatar.objects.filter(
        genero=genero_personagem,
        level_minimo__lte=profile.level,
    ).order_by("nome")
