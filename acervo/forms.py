from django import forms

from .models import Acervo


class AcervoForm(forms.ModelForm):
    class Meta:
        model = Acervo
        fields = ["titulo", "autor", "ano", "tipo", "categoria", "disponivel"]