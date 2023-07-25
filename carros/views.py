from django.shortcuts import get_object_or_404, redirect, render

from .forms import CarroForm, MarcaCarroForm
from .models import Carro


def lista_carros(request):
    carros = Carro.objects.all()
    return render(request, "lista_carros.html", {"carros": carros})


def detalhes_carro(request, carro_id):
    carro = get_object_or_404(Carro, pk=carro_id)
    return render(request, "detalhes_carro.html", {"carro": carro})


def gerenciar_carros(request):
    carros = Carro.objects.all()
    if request.method == "POST":
        form = CarroForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("gerenciar_carros")
    else:
        form = CarroForm()
    return render(request, "gerenciar_carros.html", {"form": form, "carros": carros})


def criar_marca(request):
    if request.method == "POST":
        form = MarcaCarroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("gerenciar_carros")
    else:
        form = MarcaCarroForm()
    return render(request, "criar_marca.html", {"form": form})


def editar_carro(request, carro_id):
    carro = get_object_or_404(Carro, pk=carro_id)
    if request.method == "POST":
        form = CarroForm(request.POST, request.FILES, instance=carro)
        if form.is_valid():
            form.save()
            return redirect("gerenciar_carros")
    else:
        form = CarroForm(instance=carro)
    return render(request, "editar_carro.html", {"form": form})


def deletar_carro(request, carro_id):
    carro = get_object_or_404(Carro, pk=carro_id)
    if request.method == "POST":
        carro.delete()
        return redirect("gerenciar_carros")
    return render(request, "deletar_carro.html", {"carro": carro})
