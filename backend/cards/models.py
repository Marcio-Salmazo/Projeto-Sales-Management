from django.db import models
from users.models import Customers


class Payment_Cards(models.Model):

    # Tipos pré-definidos para o atributo 'tipo'
    CARD_TYPE_CHOICES = (
        ('DEBITO', 'Débito'),
        ('CREDITO', 'Crédito'),
    )

    # Um cliente pode ter vários cartões.
    # Vendas usarão apenas ID do cartão, se aplicável.
    cliente = models.ForeignKey(Customers, on_delete=models.CASCADE)
    numero = models.CharField(max_length=20)
    nome_cartao = models.CharField(max_length=100)
    validade = models.CharField(max_length=7)  # MM/AAAA
    tipo = models.CharField(max_length=10, choices=CARD_TYPE_CHOICES)

    def __str__(self):
        # Retorno do nome do cartão em conjunto com os últimos 4 dígitos
        return f"{self.nome_cartao} - {self.numero[-4:]}"
