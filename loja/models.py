
from django.db import models

class Produto(models.Model):
    TIPO_CHOICES = [
        ('anel', 'Anel'),
        ('colar', 'Colar'),
        ('pulseira', 'Pulseira'),
        ('brinco', 'Brinco'),
        ('outro', 'Outro'),
    ]

    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    # imagem = models.ImageField(upload_to='produtos/')
    imagem = models.URLField(blank=True, null=True)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    estoque = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.nome
