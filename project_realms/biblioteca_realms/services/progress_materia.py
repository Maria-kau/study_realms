from biblioteca_realms.models import UserLibrary


# =====================================
# PROGRESSO DO CONTEÚDO
# =====================================

def get_content_progress(user, content):

    progress, created = UserLibrary.objects.get_or_create(
        user=user,
        conteudo=content
    )

    return {
        "percentage": progress.porcentagem,
        "completed": progress.concluido
    }



# =====================================
# PROGRESSO DO MÓDULO
# =====================================

def get_module_progress(user, module):

    contents = module.conteudos.all()

    total_contents = contents.count()

    completed = UserLibrary.objects.filter(
        user=user,
        conteudo__in=contents,
        concluido=True
    ).count()

    percentage = 0

    if total_contents > 0:
        percentage = (completed / total_contents) * 100

    return {
        "percentage": round(percentage, 2),
        "completed": completed,
        "total_contents": total_contents,
    }


# =====================================
# PROGRESSO DA MATÉRIA
# =====================================

def get_subject_progress(user, subject):

    modules = subject.modulos.all()


    total_contents = 0
    completed = 0


    for module in modules:

        contents = module.conteudos.all()


        total_contents += contents.count()


        completed += UserLibrary.objects.filter(
            user=user,
            conteudo__in=contents,
            concluido=True
        ).count()



    percentage = 0


    if total_contents > 0:
        percentage = (completed / total_contents) * 100


    return {
        "percentage": round(percentage, 2),
        "total_contents": total_contents,
        "completed": completed
    }



# =====================================
# ATUALIZA ÁRVORE COMPLETA
# =====================================

def refresh_progress_tree(user, content):

    module_progress = get_module_progress(
        user,
        content.modulo
    )


    subject_progress = get_subject_progress(
        user,
        content.materia
    )


    return {

        "module": module_progress,

        "subject": subject_progress

    }