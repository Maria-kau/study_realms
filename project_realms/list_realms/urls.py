from django.urls import path
from . import views

urlpatterns = [
    path("to-list/", views.to_list, name="to_list"),
    path("create-list/", views.create_list_view, name="create_list"),
    path("add-item/<int:list_id>/", views.add_item_view, name="add_item"),
    path("toggle-item/<int:item_id>/", views.toggle_item_view, name="toggle_item"),
    path("delete-item/<int:item_id>/", views.delete_item_view, name="delete_item"),
    path("delete-list/<int:list_id>/", views.delete_list_view, name="delete_list"),
]