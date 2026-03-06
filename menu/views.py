from django.shortcuts import render
from django.http import FileResponse, Http404
from .models import MenuPDF


def view_menu(request):
    menu = MenuPDF.objects.filter(is_active=True).first()
    return render(request, "menu/view_menu.html", {"menu": menu})


def menu_pdf_view(request):
    menu = MenuPDF.objects.filter(is_active=True).first()

    if not menu or not menu.pdf:
        raise Http404("No active menu PDF found.")

    response = FileResponse(menu.pdf.open("rb"), content_type="application/pdf")
    response["Content-Disposition"] = 'inline; filename="menu.pdf"'
    return response