from .models import Realm
from .services.reset import reset_weekly_realm



def realm_context(request):

    if request.user.is_authenticated:


        realm, _ = Realm.objects.get_or_create(
            user=request.user
        )


        reset_weekly_realm(
            realm
        )


        return {
            "user_realm": realm
        }


    return {
        "user_realm": None
    }