from django.db import models
from django.urls import reverse


class Acervo(models.Model):
    class Tipo(models.TextChoices):
        DIGITAL = "DIGITAL", "Digital"
        FISICO = "FISICO", "Físico"

    class Categoria(models.TextChoices):
        C000 = "000", "000 – Generalidades e Informação"
        C100 = "100", "100 – Filosofia e Psicologia"
        C200 = "200", "200 – Religião e Teologia"
        C300 = "300", "300 – Ciências Sociais e Direito"
        C400 = "400", "400 – Linguística e Idiomas"
        C500 = "500", "500 – Ciências Puras (Exatas e Naturais)"
        C600 = "600", "600 – Ciências Aplicadas (Tecnologia)"
        C700 = "700", "700 – Artes e Recreação"
        C800 = "800", "800 – Literatura"
        C900 = "900", "900 – História e Geografia"

    titulo = models.CharField("Título", max_length=200)
    autor = models.CharField("Autor", max_length=100)
    ano = models.IntegerField("Ano")
    disponivel = models.BooleanField("Disponível", default=True)
    tipo = models.CharField(
        "Tipo de acervo", max_length=7,
        choices=Tipo.choices, default=Tipo.FISICO,
    )
    categoria = models.CharField(
        "Categoria (CDD)", max_length=3,
        choices=Categoria.choices, default=Categoria.C000,
    )

    class Meta:
        verbose_name = "Acervo"
        verbose_name_plural = "Acervos"
        ordering = ["titulo"]

    def __str__(self):
        return f"{self.titulo} ({self.get_tipo_display()})"

    def get_absolute_url(self):
        return reverse("acervo:lista")