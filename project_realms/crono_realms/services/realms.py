import random
from ..models import (
    Realm,
    RealmBuilding,
    Tile
)

# =====================================
# LIMITES DE TEMPO (em minutos)
# =====================================
# Valores REAIS: árvore 30 | casa 60 | especial 1440 (1 dia) | castelo 10080 (1 semana)
# Para TESTAR, troque pelos valores de teste abaixo (crescentes!):
#   LIM_ARVORE = 1, LIM_CASA = 2, LIM_ESPECIAL = 3, LIM_CASTELO = 4
LIM_ARVORE = 30
LIM_CASA = 60
LIM_ESPECIAL = 1440
LIM_CASTELO = 10080

# =====================================
# PEGAR OU CRIAR REINO
# =====================================
def get_realm(user):
    realm, _ = Realm.objects.get_or_create(user=user)
    return realm

# =====================================
# TAMANHO DAS CONSTRUÇÕES
# =====================================
def get_building_size(tipo):
    tamanhos = {"tree": 1, "house": 2, "special": 2, "castle": 3}
    return tamanhos.get(tipo, 1)

# =====================================
# VERIFICAR ESPAÇO LIVRE
# =====================================
def position_available(realm, x, y, tamanho):
    for dx in range(tamanho):
        for dy in range(tamanho):
            if RealmBuilding.objects.filter(realm=realm, x=x + dx, y=y + dy).exists():
                return False
    return True

# =====================================
# POSIÇÃO ALEATÓRIA
# =====================================
def get_random_position(realm, tipo):
    tamanho = get_building_size(tipo)
    for _ in range(100):
        x = random.randint(0, 18 - tamanho)
        y = random.randint(0, 18 - tamanho)
        if position_available(realm, x, y, tamanho):
            return x, y
    return None, None

# =====================================
# CRIAR CONSTRUÇÃO
# =====================================
def create_building(realm, tipo):
    tile = Tile.objects.filter(tipo=tipo).order_by("?").first()
    if not tile:
        return None
    x, y = get_random_position(realm, tipo)
    if x is None:
        return None
    return RealmBuilding.objects.create(realm=realm, tile=tile, x=x, y=y)

# =====================================
# RECOMPENSA DO TEMPO (1 CONSTRUÇÃO POR SESSÃO)
# =====================================
def generate_realm(user, minutos):
    realm = get_realm(user)
    construcoes = []

    def processar_criacao(tipo):
        building = create_building(realm, tipo)
        if building:
            if tipo == "castle":
                realm.castelos += 1
                realm.total_castelos += 1
            elif tipo == "special":
                realm.especiais += 1
                realm.total_especiais += 1
            elif tipo == "house":
                realm.casas += 1
                realm.total_casas += 1
            elif tipo == "tree":
                realm.arvores += 1
                realm.total_arvores += 1
            construcoes.append(building)

    # Só a maior construção que o tempo alcança (do maior para o menor)
    if minutos >= LIM_CASTELO:
        processar_criacao("castle")
    elif minutos >= LIM_ESPECIAL:
        processar_criacao("special")
    elif minutos >= LIM_CASA:
        processar_criacao("house")
    elif minutos >= LIM_ARVORE:
        processar_criacao("tree")

    realm.save()
    return construcoes