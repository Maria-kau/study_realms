from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class TodoList(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    

    title = models.CharField(
        max_length=150
    )
    color = models.CharField(
        max_length=20,
        default="#00d0ff"
    )
    is_template = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self):
        return self.title



class TodoItem(models.Model):

    CATEGORY_CHOICES = [
        ("study", "Estudo"),
        ("work", "Trabalho"),
        ("personal", "Pessoal"),
        ("routine", "Rotina"),
        ("project", "Projeto"),
        ("others","outros")
    ]


    PRIORITY_CHOICES = [
        ("low", "Baixa"),
        ("medium", "Média"),
        ("high", "Alta"),
    ]


    todo_list = models.ForeignKey(
        TodoList,
        on_delete=models.CASCADE,
        related_name="tasks"
    )


    title = models.CharField(
        max_length=200
    )


    description = models.TextField(
        blank=True,
        null=True
    )
    color = models.CharField(
        max_length=20,
        default="#00d0ff"
    )

    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default="personal"
    )


    priority = models.CharField(
        max_length=10,
        choices=PRIORITY_CHOICES,
        default="medium"
    )


    due_date = models.DateField(
        blank=True,
        null=True
    )
    task_date = models.DateField(
        default=timezone.now
    )

    due_time = models.TimeField(
        blank=True,
        null=True
    )


    is_done = models.BooleanField(
        default=False
    )


    xp_reward = models.IntegerField(
        default=10
    )


    order = models.PositiveIntegerField(
        default=0
    )


    created_at = models.DateTimeField(
        auto_now_add=True
    )


    completed_at = models.DateTimeField(
        blank=True,
        null=True
    )


    def complete(self):

        self.is_done = True
        self.completed_at = timezone.now()
        self.save()


    def __str__(self):
        return self.title