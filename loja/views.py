from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto
from .forms import RegistroForm, ProdutoForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.urls import reverse
from utils.supabase_storage import upload_file_to_supabase

def catalogo(request):
    tipo = request.GET.get('tipo')
    preco_max = request.GET.get('preco_max')

    produtos = Produto.objects.all()

    if tipo:
        produtos = produtos.filter(tipo=tipo)
    if preco_max:
        try:
            produtos = produtos.filter(preco__lte=float(preco_max))
        except ValueError:
            pass

    total_carrinho = request.session.get('total_carrinho', 0)

    return render(request, 'loja/catalogo.html', {
        'produtos': produtos,
        'total_carrinho': total_carrinho,
        'preco_max': preco_max or 1000
    })

def sobre(request):
    total = request.session.get('total_carrinho', 0)
    return render(request, 'info/sobre.html', {'total_carrinho': total})

def contato(request):
    total = request.session.get('total_carrinho', 0)
    return render(request, 'info/contato.html', {'total_carrinho': total})

def adicionar_carrinho(request, id):
    produto = get_object_or_404(Produto, id=id)
    qtd = int(request.GET.get('qtd', 1))

    if qtd > produto.estoque:
        messages.error(request, "Quantidade solicitada maior que o estoque disponível.")
        return redirect('catalogo')

    carrinho = request.session.get('carrinho', {})
    carrinho[str(id)] = carrinho.get(str(id), 0) + qtd

    if carrinho[str(id)] > produto.estoque:
        carrinho[str(id)] = produto.estoque
        messages.warning(request, "Limite de estoque atingido para este item.")

    request.session['carrinho'] = carrinho

    # Atualizar total
    total = 0
    for pid, qtd in carrinho.items():
        p = Produto.objects.get(id=pid)
        total += p.preco * qtd
    request.session['total_carrinho'] = float(total)

    return redirect('carrinho')


def carrinho_view(request):
    carrinho = request.session.get('carrinho', {})
    itens = []
    total = 0
    for id, qtd in carrinho.items():
        produto = Produto.objects.get(pk=id)
        subtotal = produto.preco * qtd
        itens.append({'produto': produto, 'qtd': qtd, 'subtotal': subtotal})
        total += subtotal
    return render(request, 'loja/carrinho.html', {'itens': itens, 'total': total})

@require_POST
def remover_do_carrinho(request, id):
    carrinho = request.session.get('carrinho', {})
    produto_id = str(id)
    if produto_id in carrinho:
        del carrinho[produto_id]
        request.session['carrinho'] = carrinho
        # Atualizar total
        total = 0
        for pid, qtd in carrinho.items():
            p = Produto.objects.get(id=pid)
            total += p.preco * qtd
        request.session['total_carrinho'] = float(total)  # <-- converter aqui
    return redirect('carrinho')

def finalizar_compra(request):
    carrinho = request.session.get('carrinho', {})
    mensagem = 'Olá! Gostaria de comprar os seguintes itens:%0A'
    total = 0
    for id, qtd in carrinho.items():
        produto = Produto.objects.get(pk=id)
        subtotal = produto.preco * qtd
        mensagem += f"- {produto.nome} (x{qtd}): R${subtotal:.2f}%0A"
        total += subtotal
    mensagem += f"%0ATotal: R${total:.2f}"
    numero_vendedor = '5599981233892'
    link = f"https://wa.me/{numero_vendedor}?text={mensagem}"
    return redirect(link)

def registrar(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('painel')
    else:
        form = RegistroForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required(login_url='catalogo')
def painel(request):
    produtos = Produto.objects.all()
    return render(request, 'painel/produtos.html', {'produtos': produtos})

@login_required(login_url='catalogo')
def editar_produto(request, id):
    if id == 0:
        produto = None
    else:
        produto = get_object_or_404(Produto, pk=id)

    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES, instance=produto)
        if form.is_valid():
            produto = form.save(commit=False)

            if 'imagem' in request.FILES:
                file = request.FILES['imagem']
                file_bytes = file.read()
                filename = file.name

                # Função que faz upload no Supabase
                url_publica = upload_file_to_supabase(filename, file_bytes)
                
                # Atualiza o campo imagem para a URL pública
                produto.imagem = url_publica
            
            produto.save()
            return redirect('painel')
    else:
        form = ProdutoForm(instance=produto)

    return render(request, 'painel/editar.html', {'form': form})


@login_required(login_url='catalogo')
def deletar_produto(request, id):
    produto = get_object_or_404(Produto, pk=id)
    produto.delete()
    return redirect('painel')
