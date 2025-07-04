
from django.urls import path
from . import views

urlpatterns = [
    path('', views.catalogo, name='catalogo'),
    path('sobre/', views.sobre, name='sobre'),
    path('contato/', views.contato, name='contato'),
    path('carrinho/', views.carrinho_view, name='carrinho'),
    path('add/<int:id>/', views.adicionar_carrinho, name='adicionar_carrinho'),
    path('finalizar/', views.finalizar_compra, name='finalizar'),
    # path('register/', views.registrar, name='register'),
    path('painel/', views.painel, name='painel'),
    path('editar/<int:id>/', views.editar_produto, name='editar_produto'),
    path('deletar/<int:id>/', views.deletar_produto, name='deletar_produto'),
    path('carrinho/remover/<int:id>/', views.remover_do_carrinho, name='remover_do_carrinho'),
]
