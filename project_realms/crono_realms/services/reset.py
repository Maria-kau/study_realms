from django.utils import timezone

from django.utils import timezone


def reset_weekly_realm(realm):

    agora = timezone.now()


    dias_passados = (
        agora - realm.ultimo_reset
    ).days


    if dias_passados >= 7:

        realm.arvores = 0
        realm.casas = 0
        realm.especiais = 0
        realm.castelos = 0

        realm.ultimo_reset = agora

        realm.save()


    return realm