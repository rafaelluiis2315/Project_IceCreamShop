from django.shortcuts import render, get_object_or_404
from .models import Sabores
from django.http import HttpResponse, Http404
from django.core.paginator import Paginator
# Create your views here.
def index(request):
    lista_sabores = Sabores.objects.order_by('-nomes_sabor')

    sabores_paginator = Paginator(lista_sabores, 6)

    page_num = request.GET.get('page')

    page = sabores_paginator.get_page(page_num)

    page_range = sabores_paginator.page_range

    return render( request, 'sorveteria/sabores.html', {'page': page, 'page_range': page_range})

def detail(request, sabor_id):
    sabor  = get_object_or_404(Sabores, pk=sabor_id)
    return render(request, 'sorveteria/detalhe.html', {'sabor': sabor})