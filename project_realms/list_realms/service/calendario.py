from django.utils import timezone
from list_realms.models import TodoItem

def get_today_tasks(user):

    today = timezone.now().date()

    return TodoItem.objects.filter(
        todo_list__user=user,
        task_date=today
    )