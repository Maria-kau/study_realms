from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def cronograma(request):
    return render(request, "cronograma_realms/cronograma.html")
