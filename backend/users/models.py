from django.db import models
from django.contrib.auth.models import User


# A classe client representa a entidade descrita no modelo ER
# Ela herda a biblioteca Models, fornecida pelo Django
class Customers(models.Model):

    # Definição dos atributos da entidade
    # OneToOneField significa herança estendida: o perfil complementa o User.
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cpf_cnpj = models.CharField(max_length=18, blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    endereco = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.user.first_name or self.user.username


class Employee(models.Model):

    # Funcionário possui o campo funcao, conforme seu ER.
    ROLE_CHOICES = (
        ('ADMIN', 'Administrador'),
        ('SELLER', 'Vendedor')
    )

    # Definição dos atributos da entidade
    # OneToOneField significa herança estendida: o perfil complementa o User.
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cpf = models.CharField(max_length=14)
    funcao = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.user.username} ({self.funcao})"
