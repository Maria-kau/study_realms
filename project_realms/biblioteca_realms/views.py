from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def biblioteca(request):
    return render(request, "biblioteca_realms/biblioteca.html")