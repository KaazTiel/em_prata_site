
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Produto

class RegistroForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ProdutoForm(forms.ModelForm):
    imagem = forms.ImageField(required=False)  # Campo extra manual para upload
    
    class Meta:
        model = Produto
        fields = ['nome', 'tipo', 'estoque', 'descricao', 'preco']
