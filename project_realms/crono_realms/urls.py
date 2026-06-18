from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.home, name="home"),
    path("configuracao/", views.configuracao, name="configuracao"),
    path("progresso/", views.progresso, name="progresso"),
]