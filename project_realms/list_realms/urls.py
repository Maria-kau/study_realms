from django.urls import path
from . import views

urlpatterns = [
    path("to-list/", views.to_list, name="to-list"),
]