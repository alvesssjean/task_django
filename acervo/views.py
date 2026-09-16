from django.shortcuts import render
from django.http import HttpResponse
from .models import LivroDigital, LivroFisico

# Create your views here.
def inicio(request):
    return HttpResponse(
        'Olá, acervo!'
    )
    
def lista_livros_digitais(request):
    livros = LivroDigital.objects.all()
    return render(
        request, 'acervo/lista.html',
        {'livros': livros}
    )
    
def lista_livros_fisicos(request):
    livros = LivroFisico.objects.all()
    return render(
        request, 'acervo/lista.html',
        {'livros': livros}
    )