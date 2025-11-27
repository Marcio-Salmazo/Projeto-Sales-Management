from django.db import models


class Category(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


'''
    Categoria → Produto é 1:N.
    Estoque agora está dentro de produto, conforme modelado.
    SET_NULL mantém o produto caso a categoria seja removida.
'''


class Product(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade_estoque = models.IntegerField(default=0)
    categoria = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nome
