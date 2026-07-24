from django.urls import path
from . import views
from .api import study_history_api

urlpatterns = [
    path("home/", views.home, name="home"),
    path("configuracao/", views.configuracao, name="configuracao"),
    path("desenvolvimento/", views.desenvolvimento, name="desenvolvimento"),
    path("timer/", views.timer_view, name="timer"),
    path("complete-study/", views.complete_study, name="complete_study"),
    path("api/study-history/", study_history_api, name="api_study_history"),
    
]