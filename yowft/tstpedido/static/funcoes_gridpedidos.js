$(document).ready(function(){


	function montarLista() {
	   console.log("Entrei em montar lista ... ")
	   var objSelect = $(this).children();
	   var conteudoOriginal = $(objSelect).val();
	   //var conteudoOriginal = $(this).text();
       // var novoElemento = $('<select />');
       var iddoSelect = contador_itens - 1;
       var novoElementonome = 'form-'+iddoSelect+'-Produto'
       var novoElemento = $('<select name="'+novoElementonome+'" id="produto" />');
       $.each(myObj, function(a, b) {
          // console.log("Elemento de Obj = " + myObj[a].fields.produto);
          if (b.model == "tstpedido.produto") {
              var opt = document.createElement("option");
              if (b.pk == conteudoOriginal) {
                   opt.setAttribute('selected', 'selected');
                  }
              opt.value = b.pk;
              opt.innerHTML = b.pk + " - " + b.fields.nm_tipo;
              novoElemento[0].appendChild(opt);
          }
       });
     // if (
     //   $(".select-box option[value='3']").attr('selected') &&
     //   $(".select-box option[value='1986']").attr('selected')
     //    )
       $(this).html(novoElemento.bind('blur keydown', function(e) {
            var keyCode = e.which;
            var conteudoNovo = $(this).val();
            // if (keyCode == 13 && conteudoNovo != '' && conteudoNovo != conteudoOriginal) {
            if (e.type == 'blur' && conteudoNovo != '' && conteudoNovo != conteudoOriginal) {
               console.log('Entrei em tratamento para enter produto ...')
               var objTR = $(this).parent().parent();
               // var objeto = $(this).parent();
               // objeto.html(conteudoNovo);

               $.each(myObj, function(a, b) {
                 if (b.pk == conteudoNovo) {
                    console.log('Carregando Descricao, unidade, preco ...' )
                    var objDescricao = $(objTR).find('#descricao');
                    var objUnidade = $(objTR).find('#unidade');
                    var objPreco = $(objTR).find('#preco');
                    objDescricao.val(b.fields.nm_tipo);
                    $.each(myObj, function(c, d) {
                      if (d.model == 'tstpedido.unidade' && d.pk == b.fields.unidade) {
                         objUnidade.val(d.fields.abreviatura);
                         // break; ==> Deu erro de execução - Illegal break statement
                      }
                    });
                    $.each(myObj, function(e, f) {
                      if (f.model == 'tstpedido.preco' && f.fields.produto == b.pk) {
                          objPreco.val(f.fields.valor);
                         // break; ==> Deu erro de execução - Illegal break statement
                      }
                    });
                    // break;   ==> Deu erro de execução - Illegal break statement
                 };
               });  
            } else if (keyCode == 27 || e.type == 'blur') {
                // $(this).parent().html(conteudoOriginal);
                $(this).val(conteudoOriginal);
                }
            }));
       console.log("Saí de montar lista ...")
       };


    function digitaQtde() {
       console.log("conteudoOriginal - val = " + $(this).val());
       var conteudoOriginal = $(this).val();
       ///   var qInputs = $('td > input').length;
       ///   console.log("Entrei em digitaQtde. qInputs = " + qInputs);
       ///   qInputs = 0;
       ///   if (qInputs == 0) {
       ///      qInputs = 1;
       ///      iddottd = contador_itens-1;
       ///      vname = "form-"+iddotd+"-Qtde";
       ///      var novoQtde = $('<input/>', {type: 'text', value: conteudoOriginal, id: 'qtde', name: vname}).appendTo($(this));
       ///   }
       ///   $(this).children('input').html(novoQtde.bind('blur keydown', function(e) {
       /// $(this).html($(this).bind('blur keydown', function(e) {
       $(this).html($(this).bind('blur keydown', function(e) {
            console.log("$(this).text ... " + $(this).text);
            console.log("$(this).val() ... " + $(this).val());
            // $(this).text = '';
            var keyCode = e.which;
            var conteudoNovo = $(this).val();
            // if (keyCode == 13 && conteudoNovo != '' && conteudoNovo != conteudoOriginal) {
            // if (e.type == 'blur' && conteudoNovo != '' && conteudoNovo != conteudoOriginal) {
            // Código 9 = tab
            if (e.type == 'blur'  && conteudoNovo != '' && conteudoNovo != conteudoOriginal) {
               // var objeto = $(this).parent();
               // objeto.text(conteudoNovo);
               console.log("Entrei em e.type blur ... ")
               var objTR = $(this).parent().parent();
               var objPreco = $(objTR).find('#preco');
               console.log("Preco para cálculo:" + objPreco.val());
               var valor_item = Number(objPreco.val() * conteudoNovo);
               var objValorTotal = $(objTR).find('#valor_total');
               objValorTotal.val(valor_item.toFixed(2));
               // Código 27 = esc
            } else if (keyCode == 27 || e.type == 'blur') {
                console.log("Entrei em keycode 27 ... ")
                // $(this).parent().html(conteudoOriginal);
                $(this).val(conteudoOriginal);
                }
            }));
                          };
	
	function Adicionar(){
	    console.log("Entrei na função Adicionar ... ")
	    event.preventDefault()
	    if (linha_em_edicao == false)  {
	       linha_em_edicao = true;
		   contador_itens += 1;

		   iddotd = contador_itens - 1


           // OBSERVAÇÃO - na td com img src='/static/ ...' funcionou somente com o diretório static.
           // Pelos testes se for necessário um outro diretório este deve ser abaixo de static ... Deve ser restrição do Django (VERIFICAR!!!)
		   $("#tblItemPedido tbody").append(
			   "<tr>"+
			   "<td id='botoes'><img src='/static/disk.png' class='btnSalvar'> <img src='/static/delete.png' class='btnExcluir'/></td>"+
		       "<td>"+
			   "<input type=text readonly name='form-"+iddotd+"-Item' id='item' maxlength=3 value = "+contador_itens+">" +
			   "</td>" +
			   // "<td id='produto'></td>"+
    	       "<td id='tproduto'>"+
			   // "<select name='form-"+iddotd+"-Produto' id='produto' />" +
			   "</td>" +
 	    	   "<td>"+
			   "<input type=text readonly name='form-"+iddotd+"-Descrição' id='descricao' maxlength=20>" +
			   "</td>" +
			   "<td>"+
			   "<input type=text name='form-"+iddotd+"-Qtde' id='qtde' maxlength=3>" +
			   "</td>" +
			   "<td>"+
			   "<input type=text readonly name='form-"+iddotd+"-Unidade' id='unidade' maxlength=20>" +
			   "</td>" +
			   "<td>"+
			   "<input type=text readonly name='form-"+iddotd+"-Preco' id='preco' maxlength=16>" +
			   "</td>" +
			   "<td>"+
			   "<input type=text readonly name='form-"+iddotd+"-ValorTotal' id='valor_total' maxlength=16>" +
			   "</tr>");
        }
        $("#tblItemPedido tbody tr #tproduto").bind("dblclick", montarLista);
        $("#tblItemPedido tbody tr td #qtde").bind("dblclick", digitaQtde);
	    $(".btnSalvar").bind("click", Salvar);
	    // $(".btnExcluir").bind("click", Excluir);

  	};

	function Salvar(){
        var objBotoes = $(this).parent();
		objBotoes.html("<img src='/static/delete.png'class='btnExcluir'/> <img src='/static/pencil.png' class='btnEditar'/>");
        var vTotal_Pedido = 0;
        var objValorTotal;
        $("#tblItemPedido tbody tr ").each(function() {
           objValorTotal = $(this).find('#valor_total');
           if (typeof(objValorTotal.html()) != "undefined") {
           console.log("Botão Salvar. Valor de objValorTotal ..." + objValorTotal.val());
           vTotal_Pedido += Number(objValorTotal.val());
           console.log("Valor total do pedido calculado ..." + vTotal_Pedido)
           };
         });
        console.log("Replicar em #total_pedido");
        $('#id_form-TOTAL_FORMS').attr("value",contador_itens);
        $('#total_pedido').val(vTotal_Pedido.toFixed(2));
		$(".btnExcluir").bind("click", Excluir);
		linha_em_edicao = false
	};

	function Excluir(){
	    var par = $(this).parent().parent(); //tr
	    par.remove();
	};

	$("#btnAdicionar").bind("click", Adicionar); 
    $("#produto").bind("dblclick", montarLista);
});
