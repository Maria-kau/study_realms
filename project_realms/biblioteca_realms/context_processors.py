from biblioteca_realms.models import Subject
from biblioteca_realms.services.progress_materia import get_subject_progress


def biblioteca_context(request):

    if not request.user.is_authenticated:
        return {}

    materias = Subject.objects.all()

    data = []


    for materia in materias:

        progress_data = get_subject_progress(
            request.user,
            materia
        )


        data.append({

            "materia": materia,

            "progress": progress_data["percentage"],

            "total_contents": progress_data["total_contents"],

            "completed": progress_data["completed"]

        })


    return {

        "biblioteca_progress": data

    }