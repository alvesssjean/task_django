from django.contrib import admin

from .models import Acervo


@admin.register(Acervo)
class AcervoAdmin(admin.ModelAdmin):
    list_display = ("titulo", "autor", "ano", "tipo", "categoria", "disponivel")
    list_filter = ("tipo", "categoria", "disponivel")
    search_fields = ("titulo", "autor")