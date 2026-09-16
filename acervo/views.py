from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import LivroDigital, LivroFisico
from .forms import LivroForm


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
    
def novo_livro(request):
    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista')
    else:
        form = LivroForm()
    return render(request, 'acervo/form.html', {'form': form})