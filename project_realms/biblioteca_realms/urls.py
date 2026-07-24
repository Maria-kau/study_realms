from django.urls import path
from . import views


urlpatterns = [

    # ==========================
    # BIBLIOTECA (MATÉRIAS)
    # ==========================
    path(
        "biblioteca/",
        views.biblioteca_view,
        name="biblioteca"
    ),
    # ==========================
    # MÓDULOS DA MATÉRIA
    # ==========================
    path(
        "materia/<int:subject_id>/modulos/",
        views.modulo_view,
        name="subject_modules"
    ),
    # ==========================
    # CONTEÚDOS DO MÓDULO
    # ==========================
    path(
        "modulo/<int:module_id>/conteudos/",
        views.conteudos_view,
        name="module_contents"
    ),
    # ==========================
    # CONCLUIR CONTEÚDO
    # ==========================
    path(
        "conteudo/<int:content_id>/concluir/",
        views.complete_content_view,
        name="complete_content"
    ),
]