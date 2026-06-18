from django.shortcuts import render




def cronograma(request):
    return render(request, "cronograma_realms/cronograma.html")