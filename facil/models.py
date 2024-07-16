from django.db import models


class Carga_clientes(models.Model):
    id = models.AutoField(primary_key=True)
    bateria = models.CharField(max_length=30)
    numeracao_bateria = models.CharField(max_length=30)
    contato = models.CharField(max_length=13)
    valor = models.CharField(max_length=7)
    cliente = models.CharField(max_length=27)
    responsavel = models.CharField(max_length=20,blank=True, null=True)
    resolvido = models.BooleanField(default=False)


    def __str__(self):
        return self.bateria


class Assistencia(models.Model):
    id = models.AutoField(primary_key=True)
    cliente = models.CharField(max_length=30)
    bateria = models.CharField(max_length=30)
    numeracao_bateria = models.CharField(max_length=30)
    contato = models.CharField(max_length=12)
    foto = models.ImageField(upload_to='facil/', blank=True, null=True)
    responsavel = models.CharField(max_length=20, blank=True, null=True)
    resolvido = models.BooleanField(default=False)

    def __str__(self):
        return self.cliente



class Emprestimos(models.Model):
    id = models.AutoField(primary_key=True)
    cliente = models.CharField(max_length=30,blank=True, null=True)
    parceiro = models.CharField(max_length=23,blank=True, null=True)
    bateria = models.CharField(max_length=30)
    quantidade = models.CharField(max_length=100)
    numeracao_bateria = models.CharField(max_length=30)
    data = models.CharField(max_length=12)
    foto = models.ImageField(upload_to='facil/',blank=True, null=True)
    responsavel = models.CharField(max_length=20,blank=True, null=True)
    resolvido = models.BooleanField(default=False)

    
    def __str__(self):
        return self.cliente




class Seminova(models.Model):
    id = models.AutoField(primary_key=True)
    cliente = models.CharField(max_length=30,blank=True, null=True)
    contato = models.CharField(max_length=39,blank=True, null=True)
    bateria = models.CharField(max_length=30)
    valor = models.CharField(max_length=30, blank=True, null=True)
    numeracao_bateria = models.CharField(max_length=30)
    garantia = models.CharField(max_length=28,blank=True, null=True)
    data_venda = models.CharField(max_length=12)
    foto = models.ImageField(upload_to='facil/',blank=True, null=True)
    responsavel = models.CharField(max_length=20,blank=True, null=True)
    resolvido = models.BooleanField(default=False)



