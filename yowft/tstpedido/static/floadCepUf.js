function floadCepUf() {
          var option
          var selendfat = document.getElementById('endfat')
          var cep = document.getElementById('cep')
          var uf = document.getElementById('uf')
          console.log("Entrei em floadCepUf. Endereco de faturamento ..." + selendfat.value)
          for (i=0; i < myObj.length; i++) {
              if (myObj[i].pk == selendfat.value) {
                  cep.value = myObj[i].fields.cep;
                  uf.value = myObj[i].fields.uf;
                  console.log("CEP e UF ... " + cep.value + " - " + uf.value)
                                                                 }
                                            }
          }

