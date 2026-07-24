def update_class(profile, attributes):


    if profile.level < 5:

        profile.energia = "nenhuma"

        profile.classe = "iniciante"

        profile.save()

        return



    mana = (
        attributes.inteligencia +
        attributes.sabedoria
    )


    aura = (
        attributes.forca +
        attributes.destreza
    )



    if mana > aura:

        profile.energia = "mana"

        profile.classe = "mago"



    elif aura > mana:

        profile.energia = "aura"

        profile.classe = "cavaleiro"



    else:

        profile.energia = "hibrido"

        profile.classe = "cavaleiro_magico"



    profile.save()