# Generated by Django 5.2.3 on 2025-07-04 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0002_produto_estoque_produto_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='imagem',
            field=models.URLField(blank=True, null=True),
        ),
    ]
