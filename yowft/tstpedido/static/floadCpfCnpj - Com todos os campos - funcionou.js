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
          cpfcnpj.value = cliente.value
          floadEndFat(myObj, cpfcnpj.value)
                        }






