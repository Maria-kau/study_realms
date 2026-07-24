from django.urls import path
from . import views
from .api import profile_api

urlpatterns = [
    path("", views.login_view, name="login"),
    path("register/", views.register_view, name="register"),
    path("logout/", views.logout_view, name="logout"),
    path("reset-password/", views.reset_password, name="reset_password"),
    path("perfil/", views.perfil, name="perfil"),
    path("api/profile/", profile_api, name="api_profile"),
    path("perfil/avatar/",views.escolher_avatar,name="escolher_avatar"),
    path(
    "avatar/",
    views.avatar_view,
    name="avatar"
    ),

    path(
        "avatar/escolher/",
        views.escolher_avatar,
        name="escolher_avatar"
    ),
]