from django.urls import path
from .views import view_menu

urlpatterns = [
    path("menu/", view_menu, name="view_menu"),
]