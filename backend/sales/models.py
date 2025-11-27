from django.db import models
from ..users.models import Client, Employee
from ..products.models import Product


class PaymentMethod(models.Model):
    nome = models.CharField(max_length=50)
    codigo = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Sale(models.Model):
    cliente = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)
    funcionario = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)
    data = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='Concluída')
    total_final = models.DecimalField(max_digits=10, decimal_places=2)
    parcelamento = models.IntegerField(default=1)
    descricao = models.TextField(blank=True, null=True)

    metodo_pagamento = models.ForeignKey(PaymentMethod, on_delete=models.SET_NULL, null=True)

    # Campo opcional caso seja pago via cartão salvo
    cartao_usado = models.ForeignKey(
        'cards.PaymentCard',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return f"Venda {self.id} - {self.data.date()}"


# Tabela que define o relacionamento N:M
class Product_Sale(models.Model):
    venda = models.ForeignKey(Sale, on_delete=models.CASCADE, related_name='itens')
    produto = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantidade = models.IntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantidade}x {self.produto.nome}"