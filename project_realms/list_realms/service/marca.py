from django.utils import timezone

from list_realms.models import TodoItem

from usuario_realms.services.reward import reward_todo_item



def toggle_item(
        item_id,
        user=None
):

    item = TodoItem.objects.get(
        id=item_id
    )


    item.is_done = not item.is_done



    if item.is_done:

        item.completed_at = timezone.now()


        item.save()


        if user:

            reward_todo_item(

                user,

                item.category,

                item.xp_reward

            )


    else:

        item.completed_at = None

        item.save()



    return item