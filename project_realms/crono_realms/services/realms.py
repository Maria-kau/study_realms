import random
from ..models import (
    Realm,
    RealmBuilding,
    Tile
)

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
    if not tile: return None
    x, y = get_random_position(realm, tipo)
    if x is None: return None
    return RealmBuilding.objects.create(realm=realm, tile=tile, x=x, y=y)

# =====================================
# RECOMPENSA DO TEMPO (LOGICA ACUMULATIVA)
# =====================================
def generate_realm(user, minutos):
    realm = get_realm(user)
    construcoes = []

    # Cálculos das quantidades
    qtd_castelos = minutos // 10080
    qtd_especiais = minutos // 1440
    qtd_casas = minutos // 2
    qtd_arvores = minutos // 1

    # Processamento de cada tipo
    def processar_criacao(tipo, quantidade):
        for _ in range(quantidade):
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
                construcoes.append(building) # Agora acessa a lista do escopo pai

    processar_criacao("castle", qtd_castelos)
    processar_criacao("special", qtd_especiais)
    processar_criacao("house", qtd_casas)
    processar_criacao("tree", qtd_arvores)

    realm.save()
    return construcoes