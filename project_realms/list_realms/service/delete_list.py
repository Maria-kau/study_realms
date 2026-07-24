from list_realms.models import TodoItem



# =====================================
# DELETAR ITEM
# =====================================

def delete_item(item_id):

    TodoItem.objects.filter(
        id=item_id
    ).delete()



# =====================================
# DELETAR LISTA
# =====================================

def delet_list(todo_list):

    todo_list.delete()