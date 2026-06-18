#sumario:
# xp_rise_leve = xp_subir_nivel
# xp = xp_atual
# > = maior
# < = menor#
from .models import Attributes
from .models import Avatar

def upagem_xp(profile):
    xp_rise_level = profile.level * 100
    while profile.xp >= xp_rise_level:
        profile.xp -= xp_rise_level
        profile.level += 1
        xp_rise_level = profile.level * 100
    profile.save()

def gain_attribute(user, acao):

    attributes = Attributes.objects.get(user=user)

    if acao == "estudo":
        attributes.inteligencia += 2

    elif acao == "revisao":
        attributes.sabedoria += 2

    elif acao == "questoes":
        attributes.destreza += 2

    elif acao == "concluiu_sessao":
        attributes.forca += 1

    attributes.save()

def update_class(profile):
    attributes = Attributes.objects.get(user=profile.user)
    mana = attributes.inteligencia + attributes.sabedoria
    aura = attributes.destreza + attributes.forca

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

def avatars_available(profile):
    if profile.level<5:
        avatars = Avatar.objects.filter(genero=profile.genero_personagem,classe='iniciante')
    
    else:
        avatars = Avatar.objects.filter(genero=profile.genero_personagem,classe=profile.classe)

    return avatars

