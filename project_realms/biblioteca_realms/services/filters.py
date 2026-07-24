from biblioteca_realms.models import LibraryContent


# Filtrar por matéria
def filter_by_subject(subject):
    return LibraryContent.objects.filter(
        materia=subject
    )


# Filtrar por categoria
def filter_by_category(category):
    return LibraryContent.objects.filter(
        categoria=category
    )


# Filtrar por dificuldade
def filter_by_difficulty(difficulty):
    return LibraryContent.objects.filter(
        dificuldade=difficulty
    )


# Filtrar tudo junto
def filter_all(subject=None, category=None, difficulty=None):

    queryset = LibraryContent.objects.all()

    if subject:
        queryset = queryset.filter(
            materia=subject
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