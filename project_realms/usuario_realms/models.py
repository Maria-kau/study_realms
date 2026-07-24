
# 🔢 NUMÉRICOS
# IntegerField -> números inteiros (1, 2, 10)
# BigIntegerField -> números inteiros grandes
# FloatField -> números decimais (3.14)
# DecimalField -> dinheiro / precisão (99.99)

# 🔤 TEXTO
# CharField -> texto curto (nome, classe)
# TextField -> texto longo (descrições)

# 📧 ESPECIAIS DE TEXTO
# EmailField -> valida email automaticamente
# SlugField -> URL amigável (ex: meu-perfil)
# URLField -> links

# 📅 DATAS
# DateField -> data (2026-01-01)
# DateTimeField -> data + hora
# TimeField -> hora

# 🔗 RELAÇÕES (MUITO IMPORTANTE)
# ForeignKey -> muitos para um (vários progressos por user)
# OneToOneField -> um para um (user -> profile)
# ManyToManyField -> muitos para muitos (usuários em grupos)

# ✔ BOOLEANO
# BooleanField -> True ou False

# 📁 ARQUIVOS
# FileField -> arquivos gerais
# ImageField -> imagens

# ⚙️ ESPECIAIS
# JSONField -> dados em formato JSON
# UUIDField -> id único global

# 🎛️ OPÇÕES (não é field, mas usado junto)
# choices -> lista fixa de opções (select dropdown)
# default -> valor padrão
# null=True -> permite vazio no banco
# blank=True -> permite vazio no form

# avatar (raridade, classe,genero, nome imagem level)
# #
 # exemplo: user = models.OneToOneField(User, on_delete=models.CASCADE)
from django.contrib.auth.models import User
from django.db import models


class FixaUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    GENERO_USUARIO_CHOICES = [
        ('feminino', 'Feminino'),
        ('masculino', 'Masculino'),
    ]

    OBJETIVO_CHOICES = [
        ('enem', 'ENEM'),
        ('vestibular', 'Vestibular'),
        ('outro', 'Outro'),
    ]

    NIVEL_ESCOLAR_CHOICES = [
        ('1_em', '1º ano EM'),
        ('2_em', '2º ano EM'),
        ('3_em', '3º ano EM'),
        ('concluido', 'Concluído / Cursinho'),
    ]

    TURNO_ESCOLAR_CHOICES = [
        ('manha', 'Manhã'),
        ('tarde', 'Tarde'),
        ('noite', 'Noite'),
        ('flexivel', 'Flexível'),
    ]

    genero_usuario = models.CharField(max_length=20, choices=GENERO_USUARIO_CHOICES)

    objetivo = models.CharField(max_length=20, choices=OBJETIVO_CHOICES)

    tipo_universidade = models.JSONField(default=list, blank=True)  

    tipo_vestibular = models.JSONField(default=list, blank=True)

    curso = models.CharField(max_length=100, blank=True, null=True)

    nivel_escolar = models.CharField(max_length=20, choices=NIVEL_ESCOLAR_CHOICES)

    horas_estudos = models.IntegerField(default=0)

    turno_escolar = models.CharField(max_length=20, choices=TURNO_ESCOLAR_CHOICES)

    materia_dificuldade = models.JSONField(default=list, blank=True)

    def __str__(self):
        return self.user.username

def caminho_imagem_mini(instance, filename):
    return f"avatars/{instance.genero}/{instance.nome}/{instance.classe}/mini/{filename}"


def caminho_imagem_corpo(instance, filename):
    return f"avatars/{instance.genero}/{instance.nome}/{instance.classe}/corpo/{filename}"
class Avatar(models.Model):

    RARIDADE_CHOICES = [
        ('comum', 'Comum'),
        ('raro', 'Raro'),
        ('epico', 'Épico'),
        ('lendario', 'Lendário')
    ]

    raridade = models.CharField(
        max_length=20,
        choices=RARIDADE_CHOICES,
        default='comum'
    )

    CLASSE_CHOICES = [
        ('iniciante', 'Iniciante'),
        ('mago', 'Mago'),
        ('cavaleiro', 'Cavaleiro'),
        ('cavaleiro_magico', 'Cavaleiro Mágico')
    ]

    classe = models.CharField(
        max_length=20,
        choices=CLASSE_CHOICES
    )

    GENERO_CHOICES = [
        ('feminino', 'Feminino'),
        ('masculino', 'Masculino'),
    ]

    genero = models.CharField(
        max_length=20,
        choices=GENERO_CHOICES,
    )

    nome = models.CharField(
        max_length=50
    )

    imagem_mini = models.ImageField(
        upload_to=caminho_imagem_mini,
        null=True,
        blank=True,
    )

    imagem_corpo = models.ImageField(
        upload_to=caminho_imagem_corpo,
        null=True,
        blank=True
    )

    level_minimo = models.IntegerField(
        default=1
    )

    def __str__(self):

        return self.nome
# ========================================================
# PROFILE
# =========================================================

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    GENERO_PERSONAGEM_CHOICES = [
        ('feminino', 'Feminino'),
        ('masculino', 'Masculino'),
    ]

    ENERGIA_CHOICES = [
        ('nenhuma', 'Nenhuma'),
        ('mana', 'Mana'),
        ('aura', 'Aura'),
        ('hibrido', 'Híbrido'),
    ]

    genero_personagem = models.CharField(max_length=20, choices=GENERO_PERSONAGEM_CHOICES)

    energia = models.CharField(max_length=20, choices=ENERGIA_CHOICES, default='nenhuma')
    
    mana_level = models.IntegerField(default=1)
    mana_xp = models.IntegerField(default=1)

    aura_level = models.IntegerField(default=1)
    aura_xp = models.IntegerField(default=1)

    classe = models.CharField(max_length=20, choices=Avatar.CLASSE_CHOICES, default='iniciante')

    level = models.IntegerField(default=1)

    xp = models.IntegerField(default=1)

    rank = models.CharField(max_length=30, default="Iniciante")

    avatar = models.ForeignKey(
        'Avatar',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.user.username
# =========================================================
# ATTRIBUTES
# =========================================================

class Attributes(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    inteligencia = models.IntegerField(default=1)
    xp_inteligencia = models.IntegerField(default=1)

    sabedoria = models.IntegerField(default=1)
    xp_sabedoria = models.IntegerField(default=1)

    forca = models.IntegerField(default=1)
    xp_forca = models.IntegerField(default=1)

    destreza = models.IntegerField(default=1)
    xp_destreza = models.IntegerField(default=1)
# =========================================================
# PROGRESS
# =========================================================
class Progress(models.Model):
    MATERIAS = [
        ('matematica', 'Matemática'),
        ('fisica', 'Física'),
        ('quimica', 'Química'),
        ('biologia','Biologia'),
        ('historia', 'História'),
        ('geografia', 'Geografia'),
        ('sociologia','Sociologia'),
        ('filosofia','Filosofia'),
        ('literatura','Literatura'),
        ('gramatica','Gramatica'),
        ('ingles','Ingles'),
        ('espanhol','Espanhol')
    ]
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    materia = models.CharField(
        max_length=30,
        choices=MATERIAS
    )
    aulas_assistidas = models.IntegerField(
        default=0
    )
    questoes_acertadas = models.IntegerField(
        default=0
    )
    questoes_erradas = models.IntegerField(
        default=0
    )
    def total_questoes(self):
        return (
            self.questoes_acertadas
            +
            self.questoes_erradas
        )
    def media_acertos(self):
        total = self.total_questoes()
        if total == 0:
            return 0
        return (
            self.questoes_acertadas
            /
            total
        ) * 100
    def __str__(self):

        return f"{self.user.username} - {self.materia}"
    
