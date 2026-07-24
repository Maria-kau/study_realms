from ..models import StudySession
from usuario_realms.models import Profile, Attributes
from usuario_realms.services.reward import reward_timer
from crono_realms.services.realms import generate_realm

# IMPORTANTE: Importa o seu sistema de atributos e energia
from usuario_realms.services.attributes import gain_attribute

# =====================================
# REGISTRAR ESTUDO (CONECTADO AOS ATRIBUTOS)
# =====================================
def register_study(user, tipo, duracao, concluida):

    # Garante que o perfil e a tabela de atributos existam
    Profile.objects.get_or_create(user=user)
    Attributes.objects.get_or_create(user=user)

    xp = 0
    total_construcoes = 0 

    # Cria uma nova sessão no histórico
    session = StudySession.objects.create(
        user=user,
        tipo=tipo,
        duracao=duracao,
        concluida=concluida,
        xp_ganho=0
    )

    if concluida and duracao > 0:
        # 1. Entrega o XP geral do Timer ao usuário
        xp = reward_timer(
            user=user,
            tipo=tipo,
            duracao=duracao
        )

        # 2. SISTEMA RPG:
        # Captura os 3 valores retornados pela função gain_attribute
        # Se não for usar o tipo_construcao aqui, mantemos o _ para ignorar o valor
        attributes, total_construcoes, _ = gain_attribute(
            user=user, 
            tipo=tipo, 
            duracao_minutos=duracao
        )

        # 3. Chama o gerador para criar as estruturas visuais no mapa do Reino
        # Ele utiliza a lógica acumulativa que configuramos anteriormente
        generate_realm(user=user, minutos=duracao)

        # Atualiza o registro da sessão com o XP geral obtido
        session.xp_ganho = xp
        session.save(update_fields=["xp_ganho"])

    # RETORNA AMBOS: O XP ganho e a quantidade de construções geradas
    return xp, total_construcoes