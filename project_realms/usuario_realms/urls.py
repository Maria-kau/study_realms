from django.urls import path
from . import views

urlpatterns = [
    path("", views.login_view, name="login"),
    path("register/", views.register_view, name="register"),
    path("logout/", views.logout_view, name="logout"),
    path("progresso/", views.progresso, name="progresso"),
    path("reset-password/", views.reset_password, name="reset_password"),
    path("perfil/", views.perfil, name="perfil"),
]