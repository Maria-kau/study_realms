from django.db import models
from django.contrib.auth.models import User


# ==========================
# Matérias
# Ex.: Matemática, Física...
# ==========================
class Subject(models.Model):
    nome = models.CharField(
        max_length=100
    )


    def __str__(self):
        return self.nome



# ==========================
# Módulos da matéria
# ==========================
class Module(models.Model):

    nome = models.CharField(
        max_length=100
    )


    materia = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE,
        related_name="modulos"
    )


    def __str__(self):
        return f"{self.materia.nome} - {self.nome}"



# ==========================
# Conteúdos disponíveis
# Vídeos, Resumos e Questões
# ==========================
class LibraryContent(models.Model):

    CATEGORY_CHOICES = [
        ("video", "Vídeo Aula"),
        ("resumo", "Resumo"),
        ("questoes", "Questões"),
    ]


    DIFFICULTY_CHOICES = [
        ("facil", "Fácil"),
        ("medio", "Médio"),
        ("dificil", "Difícil"),
    ]


    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="conteudos"
    )


    titulo = models.CharField(
        max_length=150
    )


    descricao = models.TextField(
        blank=True
    )


    fonte = models.CharField(
        max_length=100,
        blank=True
    )


    materia = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE,
        related_name="conteudos"
    )


    modulo = models.ForeignKey(
        Module,
        on_delete=models.CASCADE,
        related_name="conteudos",
        null=True,
        blank=True
    )


    categoria = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES
    )


    dificuldade = models.CharField(
        max_length=10,
        choices=DIFFICULTY_CHOICES,
        default="medio"
    )


    duracao = models.PositiveIntegerField(
        default=0,
        help_text="Duração em segundos"
    )


    video_url = models.URLField(
        blank=True
    )


    resumo_url = models.URLField(
        blank=True
    )


    criado_em = models.DateTimeField(
        auto_now_add=True
    )


    atualizado_em = models.DateTimeField(
        auto_now=True
    )


    def __str__(self):
        return self.titulo



# ==========================
# Progresso do usuário
# ==========================
class UserLibrary(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="biblioteca"
    )


    conteudo = models.ForeignKey(
        LibraryContent,
        on_delete=models.CASCADE,
        related_name="usuarios"
    )


    favorito = models.BooleanField(
        default=False
    )


    iniciado = models.BooleanField(
        default=False
    )


    concluido = models.BooleanField(
        default=False
    )


    porcentagem = models.PositiveSmallIntegerField(
        default=0
    )


    tempo_estudado = models.PositiveIntegerField(
        default=0,
        help_text="Tempo estudado em minutos"
    )


    ultimo_acesso = models.DateTimeField(
        auto_now=True
    )


    data_inicio = models.DateTimeField(
        blank=True,
        null=True
    )


    data_conclusao = models.DateTimeField(
        blank=True,
        null=True
    )


    class Meta:
        unique_together = (
            "user",
            "conteudo"
        )


    def __str__(self):
        return f"{self.user.username} - {self.conteudo.titulo}"