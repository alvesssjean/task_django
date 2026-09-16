from django.contrib import admin
from .models import LivroDigital, LivroFisico

admin.site.register(LivroFisico)
admin.site.register(LivroDigital)
# Register your models here.
