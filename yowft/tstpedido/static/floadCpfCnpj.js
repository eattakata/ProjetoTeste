function floadEndFat(myObj, cpfcnpj) {
          var option
          var selendfat = document.getElementById('endfat')
          var cep = document.getElementById('cep')
          var uf = document.getElementById('uf')
          var i = 0
          var j = 0
          var k = 0
          // limpando o combobox
          while (selendfat.length) {
              selendfat.remove(0);
                                   }
          cep.value = ""
          uf.value = ""
          selendfat.value = ""
          for (i=0; i < myObj.length; i++) {
              if (myObj[i].fields.cliente == cpfcnpj) {
                 if (myObj[i].model == "tstpedido.endereco") {
                    if (myObj[i].fields.tp_endereco == "F") {
                       option = new Option(myObj[i].fields.logradouro, myObj[i].pk);
                       selendfat.add(option);
                       if (myObj[i].fields.fl_preferencial == "S") {
                          selendfat.selectedIndex = k;
                          cep.value = myObj[i].fields.cep;
                          uf.value = myObj[i].fields.uf;
                                                                   }
                       else {}
                       k += 1;
                                                          }
                     else {}
                                                           }
                 else {}
                                                     }
              else {}
                                             }
          }
function floadCpfCnpj() {
          var cliente = document.getElementById('id_Cliente')
          var cpfcnpj = document.getElementById('cpfcnpj')
          // Foi obrigado a colocar o inputmask abaixo porque não funcionou quando seleciona primeiro CPF e depois CNPJ
          // (a máscara ficou certa porém não vinham todos os números do CNPJ
          $("#cpfcnpj").inputmask("99.999.999/9999-99")
          cpfcnpj.value = cliente.value
          console.log("CNPJ value ... " + cpfcnpj.value + " - " + cpfcnpj.value.length)
          console.log("Cliente value ... " + cliente.value + " Cliente value length ... " + cliente.value.length)
          if (cliente.value.length == 14) {
              console.log("Entrou em length = 14")
              $("#cpfcnpj").inputmask("99.999.999/9999-99")
              }
          else
           {
              console.log("Entrou no else de length = 14")
              $("#cpfcnpj").inputmask("999.999.999-99")
          }
          // floadEndFat(myObj, cpfcnpj.value)
          floadEndFat(myObj, cliente.value)
                        }






