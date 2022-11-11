from django.shortcuts import render
from .models import Sabores
from django.http import HttpResponse, Http404
# Create your views here.
def index(request):
    lista_sabores = Sabores.objects.order_by('-nomes_sabor')
    context = {'lista_sabores': lista_sabores}
    return render( request, 'sorveteria/sabores.html', context)