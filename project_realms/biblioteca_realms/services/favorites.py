from biblioteca_realms.models import UserLibrary, LibraryContent


# Busca biblioteca do usuário
def get_user_library(user, content):

    obj, created = UserLibrary.objects.get_or_create(
        user=user,
        conteudo=content
    )

    return obj


# Adiciona aos favoritos
def add_favorite(user, content):

    library = get_user_library(user, content)

    library.favorito = True
    library.save()

    return library


# Remove dos favoritos
def remove_favorite(user, content):

    library = get_user_library(user, content)

    library.favorito = False
    library.save()

    return library


# Alterna favorito
def toggle_favorite(user, content):

    library = get_user_library(user, content)

    library.favorito = not library.favorito

    library.save()

    return library.favorito


# Verifica se é favorito
def is_favorite(user, content):

    library = get_user_library(user, content)

    return library.favorito


# Lista favoritos
def list_favorites(user):

    return LibraryContent.objects.filter(
        usuarios__user=user,
        usuarios__favorito=True
    )