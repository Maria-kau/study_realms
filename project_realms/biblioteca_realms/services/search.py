from django.db.models import Q

from biblioteca_realms.models import (
    Subject,
    Module,
    LibraryContent,
)


# =========================================================
# BUSCA INTELIGENTE
# Prioridade:
# 1 - Matérias
# 2 - Módulos
# 3 - Conteúdos
# =========================================================

def global_search(search):

    search = search.strip()

    # ==========================
    # MATÉRIAS
    # ==========================

    subjects = Subject.objects.filter(
        nome__icontains=search
    )

    if subjects.exists():

        return {
            "tipo": "materia",
            "results": subjects
        }

    # ==========================
    # MÓDULOS
    # ==========================

    modules = Module.objects.filter(
        nome__icontains=search
    )

    if modules.exists():

        return {
            "tipo": "modulo",
            "results": modules
        }

    # ==========================
    # CONTEÚDOS
    # ==========================

    contents = LibraryContent.objects.filter(

        Q(titulo__icontains=search) |
        Q(descricao__icontains=search) |
        Q(fonte__icontains=search)

    )

    return {

        "tipo": "conteudo",

        "results": contents

    }


# ========================================================
# FILTROS
# =========================================================

def filter_all(
    subject=None,
    category=None,
    difficulty=None
):

    queryset = LibraryContent.objects.all()

    if subject:

        queryset = queryset.filter(
            materia__nome__icontains=subject
        )

    if category:

        queryset = queryset.filter(
            categoria=category
        )

    if difficulty:

        queryset = queryset.filter(
            dificuldade=difficulty
        )

    return queryset