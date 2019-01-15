from django.db import models
import datetime
from django.utils import timezone

# Create your models here.

# Create your models here.
class Cliente(models.Model):
    tp_pessoa = models.CharField(max_length=2)
    cpf_cnpj = models.CharField(max_length=14, primary_key=True)
    nome_cliente = models.CharField(max_length=50)
    apelido = models.CharField(max_length=30)

    def __str__(self):
        return "CPF_CNPJ " + self.cpf_cnpj + " - " + self.apelido

    class Meta:
        db_table = 'cliente'


class Endereco(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    tp_endereco = models.CharField(max_length=1)
    fl_preferencial = models.CharField(max_length=1)
    logradouro = models.CharField(max_length=100)
    cep = models.CharField(max_length=8)
    uf = models.CharField(max_length=2)

    def __str__(self):
        return "Cliente: " +  str(self.cliente) + ", endereco: " + self.logradouro + "Cep: " + self.cep

    class Meta:
        db_table = 'endereco'

class Contato(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    nome_contato = models.CharField(max_length = 50)
    email = models.EmailField(max_length = 254)
    contato_preferencial = models.CharField(max_length = 1)
    telefone_contato = models.CharField(max_length = 11)

    def __str__(self):
        return "Cliente: " +  str(self.cliente) + ", contato: " + self.nome_contato + ",  preferencial: " + self.contato_preferencial

    class Meta:
        db_table = 'contato'

class Categoria(models.Model):
    nm_categoria = models.CharField(max_length=7, unique=True)

    def __str__(self):
        return self.nm_categoria

    class Meta:
        db_table = 'categoria'

class Especie(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nm_especie = models.CharField(max_length = 20, unique=True)

    def __str__(self):
        return "Categoria: " + str(self.categoria) + " Especie: " + self.nm_especie

    class Meta:
        db_table = 'especie'


class Unidade(models.Model):
    nm_unidade = models.CharField(max_length = 20, unique=True)
    abreviatura = models.CharField(max_length = 8, unique=True)

    def __str__(self):
        return " Abreviatura: " + self.abreviatura

    class Meta:
        db_table = 'unidade'

class Produto(models.Model):
    especie = models.ForeignKey(Especie, on_delete=models.CASCADE)
    nm_tipo = models.CharField(max_length = 20)
    cd_produto = models.CharField(max_length = 9, primary_key=True)
    unidade = models.ForeignKey(Unidade, null=True, on_delete=models.CASCADE)


    def __str__(self):
        return " Especie: " + str(self.especie) + "Tipo: " + (self.nm_tipo) + " Produto: " + self.cd_produto
    class Meta:
        db_table = 'produto'


class Preco(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits = 20, decimal_places = 2)

    def __str__(self):
        return " Produto: " + str(self.produto) + "Valor: " + str((self.valor))

    class Meta:
        db_table = 'preco'


class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data_pedido = models.DateTimeField('data pedido')
    local_entrega = models.CharField(max_length = 100)
    local_faturamento = models.CharField(max_length = 100)
    data_entrega = models.DateTimeField('data entrega')

    def __str__(self):
        return "Número Pedido: " + str(self.id) + " Cliente: " + (self.cliente) + \
               " Data do Pedido: " + self.data_pedido + "Data da Entrega: " + self.data_entrega

    class Meta:
        db_table = 'pedido'


class ItensPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    cd_produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    qtd = models.IntegerField()
    vl_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    vl_total = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return "Número Pedido: " + str(self.pedido) + " Produto: " + (self.cd_produto) + \
               " Qtde: " + str(self.qtd) + "Valor Unit: " + self.vl_unitario

    class Meta:
        db_table = 'itenspedido'