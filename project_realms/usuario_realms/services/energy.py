def update_energy(profile, tipo_energia, xp_ganho):

    if tipo_energia in [
        "inteligencia",
        "sabedoria",
        "mana"
    ]:

        profile.mana_xp += xp_ganho

        while profile.mana_xp >= (
            profile.mana_level * 100
        ):

            profile.mana_xp -= (
                profile.mana_level * 100
            )

            profile.mana_level += 1


    elif tipo_energia in [
        "forca",
        "destreza",
        "aura"
    ]:

        profile.aura_xp += xp_ganho

        while profile.aura_xp >= (
            profile.aura_level * 100
        ):

            profile.aura_xp -= (
                profile.aura_level * 100
            )

            profile.aura_level += 1


    profile.save()

    return profile