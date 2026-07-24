from django.db import models
from django.contrib.auth.models import User
# ==========================
# Matérias
# Ex.: Matemática, Física...
# ==========================
class Subject(models.Model):
    nome = models.CharField(max_length=100)
    imagem = models.ImageField(
        upload_to="biblioteca/subjects/",
        blank=True,
        null=True
    )
    def __str__(self):
        return self.nome
# ==========================
# Conteúdos disponíveis na biblioteca
# (Vídeos, Resumos e Questões)
# ==========================
class Module(models.Model):
    nome = models.CharField(max_length=100)

    materia = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE,
        related_name="modulos"
    )
    imagem = models.ImageField(
        upload_to="biblioteca/modules/",
        blank=True,
        null=True
    )

    def __str__(self):
        return f"{self.materia.nome} - {self.nome}"
    

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
    # Usuário que cadastrou o conteúdo
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="conteudos"
    )
    # Informações principais
    titulo = models.CharField(max_length=150)
    descricao = models.TextField(blank=True)
    fonte = models.CharField(
        max_length=100,
        blank=True
    )
    materia = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE,
        related_name="conteudos"
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
    # Arquivos
    thumbnail = models.ImageField(
        upload_to="biblioteca/thumbs/",
        blank=True,
        null=True
    )
    modulo = models.ForeignKey(
        Module,
        on_delete=models.CASCADE,
        related_name="conteudos",
        null=True,
        blank=True,
    )
    
    video_url = models.URLField(blank=True)
    resumo_url = models.URLField(blank=True)
    # Datas
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.titulo
# ==========================
# Progresso do usuário na biblioteca
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

    # ==========================
    # Progresso
    # ==========================
    favorito = models.BooleanField(default=False)

    iniciado = models.BooleanField(default=False)

    concluido = models.BooleanField(default=False)

    porcentagem = models.PositiveSmallIntegerField(default=0)

    tempo_estudado = models.PositiveIntegerField(
        default=0,
        help_text="Tempo estudado em minutos"
    )

    # ==========================
    # Datas
    # ==========================
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
        unique_together = ("user", "conteudo")

    def __str__(self):
        return f"{self.user.username} - {self.conteudo.titulo}"