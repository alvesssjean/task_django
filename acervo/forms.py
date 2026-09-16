from django import forms
from .models import LivroDigital, LivroFisico

class LivroForm(forms.ModelForm):
    class Meta:
        model = LivroDigital
        fields = ['titulo', 'autor', 'ano']