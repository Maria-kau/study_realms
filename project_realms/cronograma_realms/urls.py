from django.urls import path
from . import views

urlpatterns = [
    path("cronograma/", views.cronograma, name="cronograma"),
]