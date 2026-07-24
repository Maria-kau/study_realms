from django.utils import timezone

from list_realms.models import TodoList, TodoItem



# =====================================
# CRIAR LISTA
# =====================================

def create_todo_list(
        user,
        title,
        is_template=False,
        color="#00d0ff"
):

    if not title:
        raise ValueError(
            "Título não pode ser vazio"
        )


    return TodoList.objects.create(

        user=user,

        title=title.strip(),

        is_template=is_template,

        color=color

    )



# =====================================
# ADICIONAR ITEM
# =====================================

def add_item(
        todo_list,
        title,
        description=None,
        task_date=None,
        priority="medium",
        category="others",
        xp_reward=10,
        color="#00d0ff"
):

    if not title:
        raise ValueError(
            "Título não pode ser vazio"
        )


    if task_date is None:

        task_date = timezone.now().date()



    return TodoItem.objects.create(

        todo_list=todo_list,

        title=title.strip(),

        description=description,

        task_date=task_date,

        priority=priority,

        category=category,

        xp_reward=xp_reward,
        color=color

    )