from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from usuario_realms.services.reward import reward_library

from biblioteca_realms.models import (
    Subject,
    Module,
    LibraryContent,
    UserLibrary,
)


# =========================================================
# SERVICES
# =========================================================

from biblioteca_realms.services.progress import (
    update_progress,
    increase_progress,
    reset_progress,
    complete_content,
    get_percentage,
    is_completed,
)


from biblioteca_realms.services.progress_materia import (
    get_subject_progress,
    get_module_progress,
    refresh_progress_tree,
)


from biblioteca_realms.services.favorites import (
    toggle_favorite,
    list_favorites,
)


from biblioteca_realms.services.search import (
    global_search,
)


from biblioteca_realms.services.content import (
    create_content,
    update_content,
    get_content,
    list_contents,
    delete_content,
)



# =========================================================
# BIBLIOTECA
# =========================================================
@login_required
def biblioteca_view(request):

    busca = request.GET.get(
        "q",
        ""
    ).strip()


    if busca:

        resultado = global_search(
            busca
        )

        return render(

            request,

            "biblioteca_realms/biblioteca.html",

            {

                "is_search": True,

                "tipo": resultado["tipo"],

                "results": resultado["results"],

                "busca": busca,

            }

        )


    materias = []


    for materia in Subject.objects.all():

        materias.append({

            "materia": materia,

            "progress": get_subject_progress(

                request.user,

                materia

            )

        })


    return render(

        request,

        "biblioteca_realms/biblioteca.html",

        {

            "materias": materias,

            "is_search": False,

        }

    )
# =========================================================
# BUSCA
# =========================================================

@login_required
def search_view(request):

    texto = request.GET.get(
        "q",
        ""
    )


    resultado = global_search(
        texto
    )


    return JsonResponse({

        "materias":
            list(
                resultado["subjects"].values()
            ),


        "modulos":
            list(
                resultado["modules"].values()
            ),


        "conteudos":
            list(
                resultado["contents"].values()
            )

    })



# =========================================================
# MÓDULOS
# =========================================================

@login_required
def modulo_view(request, subject_id):


    materia = get_object_or_404(
        Subject,
        id=subject_id
    )


    modulos = []


    for modulo in materia.modulos.all():


        modulos.append({

            "modulo": modulo,


            "progress":
                get_module_progress(
                    request.user,
                    modulo
                )

        })


    return render(

        request,

        "biblioteca_realms/modulos.html",

        {

            "materia": materia,

            "modulos": modulos

        }

    )



# =========================================================
# CONTEÚDOS
# =========================================================

@login_required
def conteudos_view(request, module_id):


    modulo = get_object_or_404(
        Module,
        id=module_id
    )


    conteudos = []


    for conteudo in modulo.conteudos.all():


        progress, created = UserLibrary.objects.get_or_create(

            user=request.user,

            conteudo=conteudo

        )


        conteudos.append({

            "conteudo": conteudo,

            "progress": progress

        })



    return render(

        request,

        "biblioteca_realms/conteudos.html",

        {

            "modulo": modulo,

            "conteudos": conteudos,


            "module_progress":

                get_module_progress(

                    request.user,

                    modulo

                ),



            "subject_progress":

                get_subject_progress(

                    request.user,

                    modulo.materia

                )

        }

    )



# =========================================================
# PROGRESSO
# =========================================================


@login_required
def update_progress_view(request, content_id):


    content = get_object_or_404(

        LibraryContent,

        id=content_id

    )


    progress = update_progress(

        request.user,

        content,

        int(
            request.POST.get(
                "porcentagem",
                0
            )
        )

    )


    tree = refresh_progress_tree(

        request.user,

        content

    )


    return JsonResponse({

        "content_progress":
            progress.porcentagem,


        "module_progress":
            tree["module"],


        "subject_progress":
            tree["subject"]

    })




@login_required
def increase_progress_view(request, content_id):


    content = get_object_or_404(

        LibraryContent,

        id=content_id

    )


    progress = increase_progress(

        request.user,

        content,

        int(
            request.POST.get(
                "valor",
                1
            )
        )

    )


    tree = refresh_progress_tree(

        request.user,

        content

    )


    return JsonResponse({

        "content_progress":
            progress.porcentagem,


        "module_progress":
            tree["module"],


        "subject_progress":
            tree["subject"]

    })



@login_required
def complete_content_view(request, content_id):


    content = get_object_or_404(
        LibraryContent,
        id=content_id
    )


    progress, novo = complete_content(
        request.user,
        content
    )


    if novo:

        reward_library(
            request.user,
            content.categoria
        )

    tree = refresh_progress_tree(
        request.user,
        content
    )


    return JsonResponse({

        "status": "ok",

        "content_progress":
            progress.porcentagem,


        "module_progress":
            tree["module"],


        "subject_progress":
            tree["subject"]

    })


@login_required
def reset_progress_view(request, content_id):


    content = get_object_or_404(

        LibraryContent,

        id=content_id

    )


    reset_progress(

        request.user,

        content

    )


    tree = refresh_progress_tree(

        request.user,

        content

    )


    return JsonResponse({

        "status":
            "reset",


        "module_progress":
            tree["module"],


        "subject_progress":
            tree["subject"]

    })



# =========================================================
# FAVORITOS
# =========================================================


@login_required
def toggle_favorite_view(request, content_id):


    content = get_object_or_404(

        LibraryContent,

        id=content_id

    )


    favorito = toggle_favorite(

        request.user,

        content

    )


    return JsonResponse({

        "favorito":
            favorito

    })




@login_required
def favorites_list_view(request):


    favoritos = list_favorites(

        request.user

    )


    return JsonResponse({

        "results":
            list(
                favoritos.values()
            )

    })



# =========================================================
# ADMIN / CRUD CONTEÚDOS
# =========================================================


@login_required
def content_list_view(request):


    contents = list_contents()


    return JsonResponse({

        "results":
            list(
                contents.values()
            )

    })



@login_required
def content_detail_view(request, content_id):


    content = get_content(

        content_id

    )


    return JsonResponse({

        "id":
            content.id,


        "titulo":
            content.titulo,


        "descricao":
            content.descricao,


        "materia":
            content.materia.nome,


        "categoria":
            content.categoria

    })



@login_required
def content_create_view(request):


    if request.method != "POST":

        return JsonResponse(
            {
                "error":
                    "Método não permitido"
            },
            status=405
        )


    content = create_content(

        user=request.user,

        titulo=request.POST.get(
            "titulo"
        ),

        descricao=request.POST.get(
            "descricao"
        ),

        materia_id=request.POST.get(
            "materia"
        ),

        categoria=request.POST.get(
            "categoria"
        )

    )


    return JsonResponse({

        "id":
            content.id,


        "status":
            "created"

    })



@login_required
def content_delete_view(request, content_id):


    content = get_content(

        content_id

    )


    delete_content(

        content

    )


    return JsonResponse({

        "status":
            "deleted"

    })