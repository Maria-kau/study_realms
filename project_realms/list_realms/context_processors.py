from django.utils import timezone

from list_realms.models import TodoItem, TodoList


def list_block_current(request):

    if not request.user.is_authenticated:
        return {}


    hoje = timezone.now().date()


    tarefas = TodoItem.objects.filter(
        todo_list__user=request.user,
        task_date=hoje
    ).order_by("due_time")


    return {
        "tarefas_do_dia": tarefas
    }


def list_todo_progress(request):

    if not request.user.is_authenticated:
        return {}


    listas = TodoList.objects.filter(
        user=request.user
    )


    total = 0
    concluidas = 0


    for lista in listas:

        total += lista.tasks.count()

        concluidas += lista.tasks.filter(
            is_done=True
        ).count()


    pendentes = total - concluidas


    percentual = 0

    if total:
        percentual = round(
            (concluidas / total) * 100,
            2
        )


    return {
        "todo_total": total,
        "todo_concluidas": concluidas,
        "todo_pendentes": pendentes,
        "todo_progresso": percentual,
    }