function fVerBranco() {
          var vnome = document.getElementById('nome_usuario').innerHTML
          var vsobrenome = document.getElementById('sobrenome_usuario').innerHTML
          var vendereco = document.getElementById('endereco').innerHTML
          console.log(vsobrenome)
          var tam_nome = (vnome.trim()).length
          var tam_sobre = (vsobrenome.trim()).length
          var tam_ender = (vendereco.trim()).length
          if tam_nome == 0 || tam_sobre == 0 || tam_ender == 0 {
             document.getElementById('mensagem').style.visibility = "visible"
             document.getElementById('mensagem').innerHTML = "O campo não pode estar preenchido com espaços ou estar vazio"
                                                               }
                            }