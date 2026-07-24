from usuario_realms.services.xp import gain_xp
from usuario_realms.services.attributes import gain_attribute
from usuario_realms.services.player import update_player_state
from usuario_realms.services.energy import update_energy

from crono_realms.services.realms import generate_realm


# =====================================
# RECOMPENSA DA BIBLIOTECA
# =====================================

def reward_library(user, tipo):

    profile = user.profile


    gain_xp(
        profile,
        50
    )


    if tipo == "video":

        gain_attribute(
            user,
            "video_aula"
        )


    elif tipo == "resumo":

        gain_attribute(
            user,
            "resumo"
        )


    update_player_state(profile)





# =====================================
# RECOMPENSA DO CRONOGRAMA
# =====================================

def reward_schedule(user):

    profile = user.profile


    gain_xp(
        profile,
        30
    )


    gain_attribute(
        user,
        "study"
    )


    update_player_state(profile)





# =====================================
# RECOMPENSA DO TO-DO
# =====================================

def reward_todo_item(user, categoria, xp_reward):


    profile = user.profile


    # XP principal da tarefa
    gain_xp(
        profile,
        xp_reward
    )



    # atributo baseado na categoria

    if categoria == "study":

        gain_attribute(
            user,
            "study"
        )


    elif categoria == "work":

        gain_attribute(
            user,
            "work"
        )


    elif categoria == "personal":

        gain_attribute(
            user,
            "personal"
        )


    elif categoria == "routine":

        gain_attribute(
            user,
            "routine"
        )


    elif categoria == "project":

        gain_attribute(
            user,
            "project"
        )


    elif categoria == "others":

        gain_attribute(
            user,
            "others"
        )



    update_player_state(
        profile
    )



# =====================================
# RECOMPENSA DO CRONÔMETRO
# =====================================

XP_PER_MINUTE = {
    "leitura": 1,
    "video_aula": 1,
    "revisao": 1,
    "resumo": 2,
    "questoes": 2,
    "exercicios": 2,
    "redacao": 3,
    "simulado": 3,
    "outros": 1,
}


MANA_TYPES = [
    "leitura",
    "video_aula",
    "revisao",
    "resumo",
]


AURA_TYPES = [
    "questoes",
    "exercicios",
    "redacao",
    "simulado",
]

def reward_timer(user, tipo, duracao):

    profile = user.profile


    # Calcula XP pelo tempo
    xp = duracao * XP_PER_MINUTE.get(tipo, 1)


    # XP geral
    gain_xp(
        profile,
        xp
    )


    # Energia
    if tipo in MANA_TYPES:

        update_energy(
            profile,
            "mana",
            xp
        )


    elif tipo in AURA_TYPES:

        update_energy(
            profile,
            "aura",
            xp
        )


    # Atualiza jogador
    update_player_state(
        profile
    )


    # Recompensa do reino
    generate_realm(
        user,
        duracao
    )


    return xp