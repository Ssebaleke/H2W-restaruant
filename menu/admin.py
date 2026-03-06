from django.contrib import admin
from .models import MenuPDF

@admin.register(MenuPDF)
class MenuPDFAdmin(admin.ModelAdmin):
    list_display = ("title", "is_active", "uploaded_at")
    list_filter = ("is_active",)
    search_fields = ("title",)

    def save_model(self, request, obj, form, change):
        if obj.is_active:
            MenuPDF.objects.update(is_active=False)
        super().save_model(request, obj, form, change)