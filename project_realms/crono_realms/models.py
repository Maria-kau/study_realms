from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone



# =====================================
# SESSÃO DE ESTUDO
# =====================================

class StudySession(models.Model):

    TIPO_CHOICES = [
        ("leitura", "Leitura"),
        ("video_aula", "Vídeo Aula"),
        ("revisao", "Revisão"),
        ("resumo", "Resumo"),
        ("questoes", "Questões"),
        ("exercicios", "Exercícios"),
        ("redacao", "Redação"),
        ("simulado", "Simulado"),
        ("outros", "Outros"),
    ]


    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="study_sessions"
    )


    tipo = models.CharField(
        max_length=20,
        choices=TIPO_CHOICES
    )


    duracao = models.PositiveIntegerField(
        default=0
    )


    concluida = models.BooleanField(
        default=False
    )


    xp_ganho = models.PositiveIntegerField(
        default=0
    )


    criada_em = models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self):

        return f"{self.user.username} - {self.tipo}"





# =====================================
# CATÁLOGO DE TILES/CONSTRUÇÕES
# =====================================
# =====================================
# CATÁLOGO DE TILES/CONSTRUÇÕES
# =====================================

class Tile(models.Model):

    TIPO_CHOICES = [
        ("tree", "Árvore"),
        ("house", "Casa"),
        ("special", "Construção Especial"),
        ("castle", "Castelo"),
    ]


    nome = models.CharField(
        max_length=100
    )


    tipo = models.CharField(
        max_length=20,
        choices=TIPO_CHOICES
    )


    imagem = models.CharField(
        max_length=100
    )


    descricao = models.CharField(
        max_length=200,
        blank=True
    )


    # ==============================
    # TAMANHO NO MAPA ISOMÉTRICO
    # ==============================

    largura = models.PositiveIntegerField(
        default=1,
        help_text="Quantidade de tiles na horizontal"
    )


    altura = models.PositiveIntegerField(
        default=1,
        help_text="Quantidade de tiles na vertical"
    )


    # ==============================
    # AJUSTE VISUAL DA IMAGEM
    # ==============================

    offset_x = models.IntegerField(
        default=0
    )


    offset_y = models.IntegerField(
        default=-50
    )


    def __str__(self):

        return self.nome
# =====================================
# REINO DO USUÁRIO
# =====================================

class Realm(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="realm")

    # Campos de mapa atual (resetam semanalmente)
    arvores = models.PositiveIntegerField(default=0)
    casas = models.PositiveIntegerField(default=0)
    especiais = models.PositiveIntegerField(default=0)
    castelos = models.PositiveIntegerField(default=0)

    # Campos de histórico acumulado (exibidos no HTML)
    total_arvores = models.PositiveIntegerField(default=0)
    total_casas = models.PositiveIntegerField(default=0)
    total_especiais = models.PositiveIntegerField(default=0)
    total_castelos = models.PositiveIntegerField(default=0)

    ultimo_reset = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Reino de {self.user.username}"

# (Mantenha as classes Tile e RealmBuilding conforme definido no seu arquivo)



# =====================================
# CONSTRUÇÕES COLOCADAS NO MAPA
# =====================================
# =====================================
# CONSTRUÇÕES COLOCADAS NO MAPA
# =====================================

class RealmBuilding(models.Model):

    realm = models.ForeignKey(
        Realm,
        on_delete=models.CASCADE,
        related_name="buildings"
    )


    tile = models.ForeignKey(
        Tile,
        on_delete=models.CASCADE,
        related_name="placed_buildings"
    )


    # posição inicial da construção

    x = models.IntegerField()

    y = models.IntegerField()


    criada_em = models.DateTimeField(
        auto_now_add=True
    )


    class Meta:

        unique_together = (
            "realm",
            "x",
            "y"
        )


    def __str__(self):

        return f"{self.realm.user.username} - {self.tile.nome}"