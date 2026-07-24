from list_realms.models import TodoItem



# =====================================
# PEGAR ITEMS DA LISTA
# =====================================

def get_list_items(todo_list):

    return todo_list.tasks.all().order_by(
        "created_at"
    )



# =====================================
# ESTATÍSTICAS
# =====================================

def get_list_statistics(todo_list):

    total = todo_list.tasks.count()


    concluidas = todo_list.tasks.filter(
        is_done=True
    ).count()


    pendentes = total - concluidas



    percentual = 0


    if total > 0:

        percentual = round(
            (concluidas / total) * 100,
            2
        )



    return {

        "total": total,

        "concluidas": concluidas,

        "pendentes": pendentes,

        "percentual": percentual

    }