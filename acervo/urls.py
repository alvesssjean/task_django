from django.urls import path
from . import views

urlpatterns = [
    path(
        '', views.inicio,
        'livros/',
        views.lista_livros_fisicos,
        views.lista_livros_digitais,
        name='lista',
        ),
]
