from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

from biblioteca_realms.models import (
    Subject,
    Module,
    LibraryContent
)


class Command(BaseCommand):

    help = "Cria dados iniciais da biblioteca"


    def handle(self, *args, **kwargs):

        # Pega o usuário admin
        user = User.objects.filter(
            is_superuser=True
        ).first()


        if not user:
            self.stdout.write(
                self.style.ERROR(
                    "Nenhum usuário admin encontrado."
                )
            )
            return


        # ======================
        # MATÉRIAS
        # ======================

        python = Subject.objects.get_or_create(
            nome="Python"
        )[0]


        django = Subject.objects.get_or_create(
            nome="Django"
        )[0]


        matematica = Subject.objects.get_or_create(
            nome="Matemática"
        )[0]


        # ======================
        # MÓDULOS
        # ======================

        python_basico = Module.objects.get_or_create(
            nome="Fundamentos Python",
            materia=python
        )[0]


        python_poo = Module.objects.get_or_create(
            nome="Programação Orientada a Objetos",
            materia=python
        )[0]


        django_basico = Module.objects.get_or_create(
            nome="Django Básico",
            materia=django
        )[0]


        # ======================
        # CONTEÚDOS
        # ======================

        LibraryContent.objects.get_or_create(
            titulo="Variáveis em Python",
            materia=python,
            modulo=python_basico,
            user=user,
            categoria="resumo",
            dificuldade="facil",
            descricao="Aprenda variáveis, tipos de dados e valores."
        )


        LibraryContent.objects.get_or_create(
            titulo="Funções em Python",
            materia=python,
            modulo=python_basico,
            user=user,
            categoria="video",
            dificuldade="medio",
            descricao="Aprenda criar e utilizar funções."
        )


        LibraryContent.objects.get_or_create(
            titulo="Classes e Objetos",
            materia=python,
            modulo=python_poo,
            user=user,
            categoria="resumo",
            dificuldade="dificil",
            descricao="Introdução à orientação a objetos."
        )


        LibraryContent.objects.get_or_create(
            titulo="Models no Django",
            materia=django,
            modulo=django_basico,
            user=user,
            categoria="video",
            dificuldade="medio",
            descricao="Aprenda criar modelos e trabalhar com banco."
        )


        self.stdout.write(
            self.style.SUCCESS(
                "Biblioteca criada com sucesso!"
            )
        )