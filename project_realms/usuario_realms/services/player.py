from usuario_realms.models import Attributes

from .class_ import update_class
from .rank import update_rank



def update_player_state(profile):


    attributes = Attributes.objects.get(
        user=profile.user
    )



    update_class(
        profile,
        attributes
    )


    update_rank(
        profile
    )



    profile.save()


    return profile