from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import AcervoForm
from .models import Acervo


def inicio(request):
    return HttpResponse("Olá, acervo!")


def lista_livros(request):
    livros = Acervo.objects.all()

    q = request.GET.get("q", "").strip()
    tipo = request.GET.get("tipo", "")
    categoria = request.GET.get("categoria", "")

    if q:
        livros = livros.filter(Q(titulo__icontains=q) | Q(autor__icontains=q))
    if tipo in Acervo.Tipo.values:
        livros = livros.filter(tipo=tipo)
    if categoria in Acervo.Categoria.values:
        livros = livros.filter(categoria=categoria)

    return render(request, "acervo/lista.html", {
        "livros": livros,
        "tipos": Acervo.Tipo.choices,
        "categorias": Acervo.Categoria.choices,
        "q": q,
        "tipo_sel": tipo,
        "categoria_sel": categoria,
    })


def novo_livro(request):
    if request.method == "POST":
        form = AcervoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("acervo:lista")
    else:
        form = AcervoForm()
    return render(request, "acervo/form.html", {"form": form})