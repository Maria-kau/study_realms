from biblioteca_realms.models import UserLibrary


# Total de conteúdos concluídos
def total_completed(user):

    return UserLibrary.objects.filter(
        user=user,
        concluido=True
    ).count()


# Total de favoritos
def total_favorites(user):

    return UserLibrary.objects.filter(
        user=user,
        favorito=True
    ).count()


# Tempo total estudado
def total_study_time(user):

    return sum(

        item.tempo_estudado

        for item in

        UserLibrary.objects.filter(user=user)

    )


# Porcentagem média da biblioteca
def completion_percentage(user):

    biblioteca = UserLibrary.objects.filter(user=user)

    if not biblioteca.exists():
        return 0

    total = sum(

        item.porcentagem

        for item in biblioteca

    )

    return total / biblioteca.count()