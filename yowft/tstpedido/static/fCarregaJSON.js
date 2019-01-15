function fCarregaJSON() {
     var xmlhttp = new XMLHttpRequest(); 
     xmlhttp.onreadystatechange = function() {
         if (this.readyState == 4 && this.status == 200) {
             myObj = JSON.parse(this.responseText);
             console.log("Carga do JSON: " + myObj[39].model);
                                                         }
                                            }
     xmlhttp.open("GET", "carregajson", true);
     xmlhttp.send(); 
                        }