from django import forms
from . models import Cliente
# Forma1 para dar um bypass na validaçào da lista ----
from django.forms.fields import ChoiceField


# Create your forms here.

#  Forma1 para dar um bypass na validaçào da lista ----  #####
class ChoiceFieldNoValidation(ChoiceField):
    def validate(self, value):
        pass


class DadosCliente(forms.Form):

    Lista_clientes = [('Selecione', '------')] + [(s[0], s[1]) for s in Cliente.objects.values_list('cpf_cnpj', 'apelido')]
    Cliente = forms.ChoiceField(widget=forms.Select(attrs={'onclick': 'floadCpfCnpj()', 'value': ''}), choices=Lista_clientes)
    CPF_CNPJ = forms.CharField(max_length=18, widget=forms.TextInput(attrs={'id': 'cpfcnpj', 'readonly': True}))
    Lista_enderecos = [('Selecione', '------')]
    #  Forma1 para dar um bypass na validaçào da lista ----  #####
    Endereco_Faturamento = ChoiceFieldNoValidation(widget=forms.Select(attrs={'id': 'endfat', 'onclick': 'floadCepUf()', 'size': 1}), choices=Lista_enderecos)
    Cep = forms.CharField(max_length=9, widget=forms.TextInput(attrs={'id': 'cep'}))
    UF = forms.CharField(max_length=2, widget=forms.TextInput(attrs={'id': 'uf'}))

class ItensPedidoF(forms.Form):
    Ação = forms.CharField(max_length=1, widget=forms.TextInput(attrs={'id': 'botoes', 'readonly': True}), required=False)
    Item = forms.CharField(max_length=3, widget=forms.TextInput(attrs={'id': 'item', 'readonly': True}), required=False)
    # Produto = forms.CharField(max_length=9, widget=forms.TextInput(attrs={'id': 'produto'}), required=False)
    Lista_produto = [('Selecione', '------')]
    Produto = ChoiceFieldNoValidation(widget=forms.Select(attrs={'id': 'produto'}), choices=Lista_produto, required=False)
    Descrição = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'id': 'descricao', 'readonly': True}), required=False)
    Qtde = forms.CharField(max_length=3, widget=forms.TextInput(attrs={'id': 'qtde'}), required=False)
    Unidade = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'id': 'unidade', 'readonly': True}), required=False)
    Preco = forms.CharField(max_length=16, widget=forms.TextInput(attrs={'id': 'preco', 'readonly': True}), required=False)
    ValorTotal = forms.CharField(max_length=16,  initial=0, widget=forms.TextInput(attrs={'id': 'valor_total', 'readonly': True}), required=False)

class TotalPedido(forms.Form):
    ValorTotalPedido = forms.CharField(max_length = 16, initial=0,  widget=forms.TextInput(attrs={'id': 'total_pedido', 'readonly': True}))

