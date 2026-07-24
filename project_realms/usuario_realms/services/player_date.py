from usuario_realms.models import (
    Profile,
    Attributes,
    FixaUsuario,
    Avatar
)
from .avatrs import avatars_available


def get_player_data(user):

    fixa_usuario, _ = FixaUsuario.objects.get_or_create(
        user=user
    )

    profile, created = Profile.objects.get_or_create(
        user=user
    )

    if created:
        profile.xp = 1
        profile.mana_xp = 1
        profile.aura_xp = 1
        profile.mana_level = 1
        profile.aura_level = 1
        profile.level = 1
        profile.energia = "nenhuma"
        profile.classe = "iniciante"
        profile.save()

    attributes, _ = Attributes.objects.get_or_create(
        user=user
    )

    return {

        "profile": profile,
        "fixaUsuario": fixa_usuario,
        "attributes": attributes,

        "xp_current": profile.xp,
        "xp_max": profile.level * 100,

        "mana_current": profile.mana_xp,
        "mana_max": profile.mana_level * 100,

        "aura_current": profile.aura_xp,
        "aura_max": profile.aura_level * 100,

        "default_avatar": avatars_available(profile).order_by("level_minimo", "nome").first()

    }