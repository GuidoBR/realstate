from django.shortcuts import render, get_object_or_404
from .models import Imovel

def index(request):
    return render(request, "index.html", {})

def about(request):
    return render(request, "quem-somos.html", {'title': 'Quem somos'})

def imovel_index(request):
    latest_imoveis = Imovel.objects.order_by('-updated_at')[:5]
    context = { 'imoveis': latest_imoveis}
    return render(request, "venda-de-imoveis.html", context)

def imovel_view(request, imovel_id):
    imovel = get_object_or_404(Imovel, pk=imovel_id)
    return render(request, "imovel/ver.html", {"imovel": imovel})

def aluguel_residencial(request):
    latest_imoveis = Imovel.objects.order_by('-updated_at')[:5]
    context = { 'imoveis': latest_imoveis}
    return render(request, "aluguel-residencial.html", context)

def aluguel_comercial(request):
    latest_imoveis = Imovel.objects.order_by('-updated_at')[:5]
    context = { 'imoveis': latest_imoveis}
    return render(request, "aluguel-comercial.html", context)

def aluguel_temporada(request):
    latest_imoveis = Imovel.objects.order_by('-updated_at')[:5]
    context = { 'imoveis': latest_imoveis}
    return render(request, "aluguel-temporada.html", context)
