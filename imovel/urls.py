from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:imovel_id>/', views.get, name='get'),
]