from django.shortcuts import render, get_object_or_404
from .models import Imovel

def index(request):
    return render(request, 'imovel/index.html')

def get(request, imovel_id):
    imovel = get_object_or_404(Imovel, pk=imovel_id)
    return render(request, 'imovel/get.html', {'imovel': imovel})