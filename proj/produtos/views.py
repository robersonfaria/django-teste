from django.shortcuts import render
from .models import Produto


def home(request):
    nome = 'Roberson'
    produtos = Produto.objects.all()
    return render(request, 'produtos.html', {'nome': nome, 'produtos': produtos})


def produto(request, id):
    produto = Produto.objects.get(id=id)
    return render(request, 'produto.html', {'produto': produto})