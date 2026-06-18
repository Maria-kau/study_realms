from django.urls import path
from . import views

urlpatterns = [
    path("biblioteca/", views.biblioteca, name="biblioteca"),
]