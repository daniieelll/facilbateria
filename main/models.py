from django.db import models

# Definindo o modelo Bateria se ele não estiver definido
class Bateria(models.Model):
    nome = models.CharField(max_length=100)
    capacidade = models.IntegerField()

    def __str__(self):
        return self.nome

# Defina o modelo Cliente
class Cliente(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

# Definindo os outros modelos
class CargaClientes(models.Model):
    bateria = models.CharField(max_length=100)
    numeracao = models.CharField(max_length=100)
    contato = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    responsavel = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.cliente} - {self.bateria}"

class Assistencia(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    # Outros campos relevantes

class GarantiaSeminova(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    # Outros campos relevantes

class Emprestimos(models.Model):
    bateria = models.ForeignKey(Bateria, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data_emprestimo = models.DateTimeField(auto_now_add=True)
    data_devolucao = models.DateTimeField(null=True, blank=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.cliente} - {self.bateria}"
