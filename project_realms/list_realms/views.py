from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def to_list(request):
    return render(request, "list_realms/to-list.html")