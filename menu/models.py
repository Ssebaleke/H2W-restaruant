from django.db import models

class MenuPDF(models.Model):
    title = models.CharField(max_length=120, default="Our Menu")
    pdf = models.FileField(upload_to="menus/")
    is_active = models.BooleanField(default=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-uploaded_at"]

    def __str__(self):
        return f"{self.title} ({'active' if self.is_active else 'inactive'})"