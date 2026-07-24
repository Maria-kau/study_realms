from django.utils import timezone

from biblioteca_realms.models import UserLibrary


# Busca progresso
def get_progress_user(user, content):

    obj, created = UserLibrary.objects.get_or_create(
        user=user,
        conteudo=content
    )

    return obj


# Atualiza progresso
def update_progress(user, content, porcentagem):

    progress = get_progress_user(user, content)

    progress.porcentagem = max(
        0,
        min(100, porcentagem)
    )

    if progress.porcentagem == 100:

        progress.concluido = True
        progress.data_conclusao = timezone.now()

    progress.save()

    return progress


# Soma progresso
def increase_progress(user, content, valor):

    progress = get_progress_user(user, content)

    progress.porcentagem = min(
        100,
        progress.porcentagem + valor
    )

    if progress.porcentagem == 100:

        progress.concluido = True
        progress.data_conclusao = timezone.now()

    progress.save()

    return progress


# Marca como concluído
def mark_as_completed(user, content):

    progress = get_progress_user(user, content)

    progress.porcentagem = 100
    progress.concluido = True
    progress.data_conclusao = timezone.now()

    progress.save()

    return progress


# Reinicia progresso
def reset_progress(user, content):

    progress = get_progress_user(user, content)

    progress.porcentagem = 0
    progress.concluido = False
    progress.data_conclusao = None

    progress.save()

    return progress


# Verifica se concluiu
def is_completed(user, content):

    progress = get_progress_user(user, content)

    return progress.concluido


# Retorna progresso
def get_percentage(user, content):

    progress = get_progress_user(user, content)

    return progress.porcentagem




def complete_content(user, content):

    progress, created = UserLibrary.objects.get_or_create(
        user=user,
        conteudo=content
    )


    if progress.concluido:
        return progress, False


    progress.concluido = True
    progress.porcentagem = 100
    progress.save()


    return progress, True