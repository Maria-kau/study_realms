from .services.player_date import get_player_data


def player_context(request):

    if not request.user.is_authenticated:
        return {}

    return get_player_data(request.user)