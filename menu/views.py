from django.shortcuts import render
from .models import MenuPDF

def view_menu(request):

    menu = MenuPDF.objects.filter(is_active=True).first()

    return render(
        request,
        "menu/view_menu.html",
        {"menu": menu}
    )