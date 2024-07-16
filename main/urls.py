from django.urls import path
from . import views  # Importe as views do seu aplicativo main

urlpatterns = [
    path('', views.baseView, name='base_lista'),
    path('assistencia/', views.AssistenciaView, name='assistencia_lista'),
    path('emprestimos/', views.EmprestimosView, name='emprestimos_lista'),
    path('carga_clientes/', views.criar_carga_clientes, name='carga_clientes_lista'),  # Corrigido para usar criar_carga_clientes
    path('garantia_seminovas/', views.GarantiaSeminovaView, name='garantia_seminovas_lista'),
]
