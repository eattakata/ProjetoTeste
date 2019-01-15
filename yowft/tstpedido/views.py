from django.shortcuts import render
from django.http import HttpResponse, FileResponse
from django.utils import timezone
from django.core import serializers
from .models import Cliente, Contato, Endereco, Produto, Unidade, Preco, Pedido, ItensPedido
from .forms import DadosCliente, ItensPedidoF, TotalPedido
from django.forms.formsets import formset_factory
from datetime import timedelta
from django.core.mail import EmailMessage
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, letter
from shutil import make_archive

from django.http import HttpResponse
import csv




# from django.core.mail import send_mail #


# Create your views here.
def index(request):
    #     return HttpResponse("Boa noite, estamos tentando funcionar o aplicativo.")
    tmp = []
    context = {'acesso': tmp}
    return render(request, 'tstpedido/index.html', context)


def dadoslogin(request):
    # FORMA 1 - funcionou ok #
    # tmp = [request.POST.get('nome'), request.POST.get('sobrenome'), request.POST.get('endereco')]
    # context = {'dados': tmp}

    # FORMA 2 #
    # context = {'nome': request.POST.get('nome'), 'sobrenome': request.POST.get('sobrenome'),
    #            'endereco': request.POST.get('endereco')}
    # return render(request, 'tstpedido/dadoslogin.html', context)

    # ---- Não precisou da validação abaixo. Foi resolvido com JavaScript. Se o campo tem o atributo "required" a tela continua.
    # A forma encontrada foi eliminar os brancos à dir e esquerda do campo digitado. De resto o html faz sozinho
    # if context['nome'].strip() == '' or context['sobrenome'].strip() == '' or context['endereco'].strip() == '':
    #     return HttpResponse("Não há dados")
    # else:
    #     return HttpResponse(context)
    # endif

    # FORMA 3 para habilitar Familia e/ou Amigos na tela principal de acordo com a lista #
    tmp = ['pedidos', 'amigo']
    context = {'acesso': tmp}
    return render(request, 'tstpedido/index.html', context)


def pedidos(request):
    ItensFormSet = formset_factory(ItensPedidoF)

    if request.method == 'POST':
        # # create a form instance and populate it with data from the request:
        ### return HttpResponse("Seu pedido foi gravado com sucesso. O número é: " + str(fgravaPedido(form, item_formset, total_pedido)))
        form = DadosCliente(request.POST)
        item_formset = ItensFormSet(request.POST)
        total_pedido = TotalPedido(request.POST)

        if form.is_valid() and item_formset.is_valid() and total_pedido.is_valid():
            num_pedido = fgravaPedido(form, item_formset, total_pedido)
            # send_mail - usado quando não há arquivo atachaoo. É um método simplficado do EmailMessage
            # send_mail('PEDIDO APROVADO', 'Seu pedido foi aprovado. O número dele é: ' + str(num_pedido), 'empresakenmei@outlook.com',
            #           ['empresakenmei@outlook.com'], fail_silently=False)
            arquivo_csv = fgeraCSV(form, item_formset, total_pedido, num_pedido)
            arquivo_pdf = fgeraPDF()
            fgeraarchive()
            email = EmailMessage(
                'TESTE COM PEDIDOS', 'O número do pedido é: ' + str(num_pedido),
                'empresakenmei@outlook.com', ['empresakenmei@outlook.com'])
            # email.attach_file(fgeraCSV(form, item_formset, total_pedido, num_pedido), fgeraPDF()) ==> só funcionou com 1 arquivo atachado
            email.attach_file(arquivo_pdf)
            email.send()
            return HttpResponse(
                "Seu pedido foi gravado com sucesso. A confirmação do seu pedido foi enviado para o email 'empresakenmei@hotmail.com'")
        else:
            return HttpResponse('Formulário não é válido')
    else:
        # # lista usada somente para teste
        lista = [{'Ação': '', 'Item': '1', 'Produto': 'Laran-002', 'Descrição': 'Lima', 'Qtde': '15', 'Unidade': 'dz',
                  'Preco': '12.33', 'ValorTotal': '184.95'},
                 {'Ação': '', 'Item': '2', 'Produto': 'Alfac-005', 'Descrição': 'Romana', 'Qtde': '20',
                  'Unidade': 'pacote', 'Preco': '5.98', 'ValorTotal': '119.60'}]
        # ipedidoformset = ItensFormSet(initial=lista)

        form = DadosCliente()
        ipedidoformset = ItensFormSet()
        form2 = TotalPedido()

        #    Gerar um JSON - dados do cliente:
        all_objects = list(Cliente.objects.all()) + list(Contato.objects.all()) + list(Endereco.objects.all()) \
                      + list(Produto.objects.all()) + list(Unidade.objects.all()) + list(Preco.objects.all())
        with open("tstpedido\\templates\dados.json", "w") as saida:
            serializers.serialize("json", all_objects, stream=saida)
        ####  Para obter dados da classe META
        ####  return HttpResponse(request.META['SERVER_NAME'])
        ###  ---  return render(request, 'tstpedido/pedidos.html', {'form': form, 'ItensPedido': ipedido_formset, 'form2': form2})
        return render(request, 'tstpedido/pedidos.html', {'form': form, 'formset1': ipedidoformset, 'form2': form2})


def fgravaPedido(form, item_formset, total_pedido):
    aux = Endereco.objects.get(id=form.cleaned_data['Endereco_Faturamento'])
    vpedido = Pedido(data_pedido=timezone.now(), local_entrega=aux.logradouro, local_faturamento=aux.logradouro, \
                     data_entrega=timezone.now() + timedelta(days=3), cliente_id=form.cleaned_data['Cliente'])
    vpedido.save()
    idPedido = vpedido.id

    for item_form in item_formset:
        iQtde = int(item_form.cleaned_data.get('Qtde'))
        vitemPedido = ItensPedido(pedido_id=idPedido, cd_produto_id=item_form.cleaned_data.get('Produto'), \
                                  qtd=iQtde, vl_unitario=item_form.cleaned_data.get('Preco'), \
                                  vl_total=item_form.cleaned_data.get('ValorTotal'), \
                                  )
        vitemPedido.save()

        #  qtd = item_form.cleaned_data.get('Qtde')
        #  vl_unitario = item_form.cleaned_data.get('Preco')
        #  vl_total = item_form.cleaned_data.get('ValorTotal')
        #  produto = item_form.cleaned_data.get('Produto')
        #  d = d + ' Qtde ...' + qtd + ' Valor Unitario ...' + vl_unitario + ' Valor Total ... ' + vl_total + ' Produto ... ' + produto
    #  c = "Valor total: " + total_pedido.cleaned_data['ValorTotalPedido']
    #  resultado = a + c + d
    return idPedido


def fgeraCSV(form, item_formset, total_pedido, num_pedido):
    arquivoOutput = 'tstpedido\\static\pedido_' + str(num_pedido) + '.csv'
    aux = Endereco.objects.get(id=form.cleaned_data['Endereco_Faturamento'])
    with open(arquivoOutput, 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=';', quoting=csv.QUOTE_MINIMAL)
    # response = HttpResponse(content_type='text/csv')
    # response['Content-Disposition'] = 'attachment; filename=' + 'Pedido - ' + str(num_pedido) + str(timezone.now()) + '.csv'
    # response['Content-Disposition'] = 'filename=Pedido.csv'
    # writer = csv.writer(response, csv.excel)
    # response.write(u'\ufeff'.encode('utf8'))  # BOM (optional...Excel needs it to open UTF-8 file properly)
        writer.writerow(["Cliente","Endereço","CEP", "UF"])
        writer.writerow([
            form.cleaned_data['Cliente'],
            aux.logradouro,
            form.cleaned_data['Cep'],
            form.cleaned_data['UF']
            ])
        writer.writerow([
            'Produto',
            'Descrição',
            'Unidade',
            'Preço',
            'Qtde',
            'Valor Total'
        ])

        for item_form in item_formset:
            iQtde = int(item_form.cleaned_data.get('Qtde'))
            writer.writerow([
                item_form.cleaned_data.get('Produto'),
                item_form.cleaned_data.get('Descrição'),
                item_form.cleaned_data.get('Unidade'),
                item_form.cleaned_data.get('Preco'),
                iQtde,
                item_form.cleaned_data.get('ValorTotal')
            ])
        writer.writerow([
            'Valor Total do Pedido'
        ])
        writer.writerow([
            total_pedido.cleaned_data['ValorTotalPedido']
        ])

    return arquivoOutput

def fgeraPDF():
    # Create the PDF object, using the buffer as its "file."
    nome_arquivo = "tstpedido\\static\hello2.pdf"
    p = canvas.Canvas(nome_arquivo, pagesize=A4)

    p.setLineWidth(.3)
    p.setFont('Helvetica', 12)

    p.drawString(30, 750, 'PEDIDO DE COMPRA')
    p.drawString(30, 735, 'EMPRESAS TESTE')
    p.drawString(500, 750, "04/01/2019")
    p.line(480, 747, 580, 747)

    p.drawString(275, 725, 'VALOR TOTAL:')
    p.drawString(500, 725, "R$ 10.000,00")
    p.line(378, 723, 580, 723)

    p.save()

    return nome_arquivo

def fgeraarchive():
    archive_name = "tstpedido\\archives\\"
    root_dir = "tstpedido\\static"
    make_archive(archive_name, 'zip', root_dir)

    return

def cadastrojson(request):
    return HttpResponse(saida)
