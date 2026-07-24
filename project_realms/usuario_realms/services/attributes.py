from usuario_realms.models import Attributes
from usuario_realms.services.energy import update_energy

def gain_attribute(user, tipo, duracao_minutos=None):
    attributes = Attributes.objects.get(user=user)
    profile = user.profile

    # Lógica de definição de tipo e quantidade
    # 1 dia = 1440 min | 1 semana = 10080 min
    if duracao_minutos is None:
        # To-Do padrão: Dá 1 árvore
        total_construcoes = 1
        tipo_construcao = 'tree'
    elif duracao_minutos >= 10080:
        total_construcoes = duracao_minutos // 10080
        tipo_construcao = 'castle'
    elif duracao_minutos >= 1440:
        total_construcoes = duracao_minutos // 1440
        tipo_construcao = 'special'
    elif duracao_minutos >= 60:
        total_construcoes = duracao_minutos // 60
        tipo_construcao = 'house'
    else:
        # Padrão para tempos menores que 60min (ex: 30min)
        total_construcoes = max(1, duracao_minutos // 30)
        tipo_construcao = 'tree'

    # Regra de negócio (XP/Energia multiplicados pelo total)
    xp_ganho = total_construcoes * 20
    pontos_energia = total_construcoes * 10

    atributo = None

    # Mapeamento e distribuição do XP
    if tipo == "video_aula":
        attributes.xp_inteligencia += xp_ganho
        atributo = "inteligencia"
    elif tipo in ["resumo", "leitura", "revisao"]:
        attributes.xp_sabedoria += xp_ganho
        atributo = "sabedoria"
    elif tipo in ["questoes", "exercicios", "simulado"]:
        attributes.xp_forca += xp_ganho
        atributo = "forca"
    elif tipo in ["redacao", "outros"]:
        attributes.xp_destreza += xp_ganho
        atributo = "destreza"

    if atributo:
        update_energy(profile, atributo, pontos_energia)

    level_up_attribute(attributes)
    
    attributes.save()
    profile.save()

    # Retorna o total e o tipo para o service de geração de mapa saber o que criar
    return attributes, total_construcoes, tipo_construcao

def level_up_attribute(attributes):
    # (Mantido igual, apenas garantindo que os loops funcionem)
    for attr in ['inteligencia', 'sabedoria', 'forca', 'destreza']:
        xp_attr = f'xp_{attr}'
        while getattr(attributes, xp_attr) >= 100:
            setattr(attributes, xp_attr, getattr(attributes, xp_attr) - 100)
            setattr(attributes, attr, getattr(attributes, attr) + 2)
    attributes.save()