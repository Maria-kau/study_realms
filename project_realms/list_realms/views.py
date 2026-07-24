from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from list_realms.models import TodoList, TodoItem
from list_realms.service.create_list import(create_todo_list,add_item)
from list_realms.service.marca import(toggle_item)
from list_realms.service.delete_list import(delete_item,delet_list)
from list_realms.service.search_progress import(get_list_items,get_list_statistics)

@login_required
def to_list(request): # Deixe sem o list_id nos argumentos da função
    lists = TodoList.objects.filter(user=request.user)
    
    # Pegamos o ID diretamente da URL (?list_id=X)
    list_id = request.GET.get('list_id')
    
    selected_list = None
    items = []

    if list_id:
        selected_list = get_object_or_404(TodoList, id=list_id, user=request.user)
        items = selected_list.tasks.all()

    return render(
        request,
        "list_realms/to-list.html",
        {
            "lists": lists,
            "selected_list": selected_list,
            "items": items,
        }
    )


def create_list_view(request):

    if request.method == "POST":

        title = request.POST.get("title")
        color = request.POST.get("color")

        create_todo_list(
            user=request.user,
            title=title,
            color=color
        )

        return redirect("to_list")

@login_required
def add_item_view(request, list_id):

    todo_list = get_object_or_404(
        TodoList,
        id=list_id,
        user=request.user
    )


    if request.method == "POST":

        title = request.POST.get("title")
        category = request.POST.get("category", "personal")
        color = request.POST.get("color")

        add_item(
            todo_list=todo_list,
            title=title,
            category=category,
            xp_reward=50,
            color=color
        )


    return redirect("to_list")



@login_required
def toggle_item_view(request, item_id):

    item = get_object_or_404(
        TodoItem,
        id=item_id,
        todo_list__user=request.user
    )


    toggle_item(
        item.id,
        user=request.user
    )


    return redirect("to_list")



@login_required
def delete_item_view(request, item_id):

    item = get_object_or_404(
        TodoItem,
        id=item_id,
        todo_list__user=request.user
    )


    delete_item(
        item.id
    )


    return redirect("to_list")



@login_required
def delete_list_view(request, list_id):

    todo_list = get_object_or_404(
        TodoList,
        id=list_id,
        user=request.user
    )


    delet_list(
        todo_list
    )


    return redirect("to_list")



@login_required
def todo_detail(request, list_id):

    todo_list = get_object_or_404(
        TodoList,
        id=list_id,
        user=request.user
    )


    items = get_list_items(
        todo_list
    )


    progress = get_list_statistics(
        todo_list
    )


    return render(
        request,
        "list_realms/to-list.html",
        {
            "todo_list": todo_list,
            "items": items,
            "progress": progress
        }
    )