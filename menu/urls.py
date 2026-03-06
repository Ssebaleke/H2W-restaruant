from django.urls import path
from .views import view_menu, menu_pdf_view

urlpatterns = [
    path("menu/", view_menu, name="view_menu"),
    path("menu/view/", menu_pdf_view, name="menu_pdf_view"),
]