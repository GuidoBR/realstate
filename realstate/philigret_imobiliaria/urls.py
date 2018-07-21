from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('quem-somos/', views.about, name='quem-somos'),
	path('venda-de-imoveis/', views.imovel_index, name='venda-de-imoveis'),
        path('venda-de-imoveis/<int:imovel_id>', views.imovel_view, name='detalhes-imovel'),
	path('aluguel-residencial/', views.aluguel_residencial, name='aluguel-residencial'),
	path('aluguel-comercial/', views.aluguel_comercial, name='aluguel-comercial'),
	path('aluguel-por-temporada/', views.aluguel_temporada, name='aluguel-por-temporada'),
	]
