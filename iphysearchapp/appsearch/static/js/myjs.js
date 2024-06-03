function onloadpagewelcome() {  //en welcome
    var selectBox = document.getElementById("selectdbwel");
    var elementoplace =selectBox.options[0].value;
    document.getElementById("iddbselectedwel").value = elementoplace; 
    return;
}

function onloadpagbuscaips() {  //en buscar ips
    var selectBox = document.getElementById("selectdb");
    var elementoplace =selectBox.options[0].value;
    document.getElementById("idtxtdb").value = elementoplace; 
    document.getElementById("idtxtdbrbs").value = elementoplace;
    var tituloIps = document.getElementById("ips");
    tituloIps.classList.add("font-weight-bold", "text-white");
    return;
}

function onloadpageimpacto() { //en impacto
    var selectBox = document.getElementById("selectdb");
    var elementoplace =selectBox.options[0].value;
    document.getElementById("idtxtdb").value = elementoplace; 
    return;
}
function onloadpagesaturaciones() { //en saturaciones
    var selectBox = document.getElementById("selectdb");
    var elementoplace =selectBox.options[0].value;
    document.getElementById("idtxtdb").value = elementoplace; 
    return;
}

function onloadpagesgraficas() { //en saturaciones
    var selectBox = document.getElementById("selectdb");
    var elementoplace =selectBox.options[0].value;
    document.getElementById("idtxtdb").value = elementoplace; 
    return;
}

function onloadpagevarios() { //
    var selectBox = document.getElementById("selectdb");
    var elementoplace =selectBox.options[0].value;
    document.getElementById("idtxtdb").value = elementoplace; 
    return;
}

function onloadpagesmantenimiento() { //en saturaciones
    var tituloIps = document.getElementById("mantenimiento");
    tituloIps.classList.add("font-weight-bold", "text-white");
    return;
}

function onloadpagesabout() { //en about
    var tituloIps = document.getElementById("about");
    tituloIps.classList.add("font-weight-bold", "text-white");
    return;
}


function copiaripnodo(ipnodo) { //en buscarip
    document.getElementById("idtxtip").value = ipnodo;
    return;
}

function copiaselectdbs(){ //en welcome select dbs
    var selectedValue = document.getElementById('selectdbwel').value;
    document.getElementById('iddbselectedwel').value = selectedValue;
}

function copiaselectdbsrbs(){ //en welcome select dbs
    var selectedValue = document.getElementById('selectdb').value;
    document.getElementById('dbrbs').value = selectedValue;
}

function agregafechahora() { 
    const fechaActual = new Date();
    const dia = fechaActual.getDate();
    const mes = fechaActual.getMonth() + 1;  
    const año = fechaActual.getFullYear();
    const hora = fechaActual.getHours();
    const minutos = fechaActual.getMinutes().toString().padStart(2, "0"); 
    document.getElementById("idfechahora").value = `${dia}/${mes}/${año} ${hora}:${minutos} `;
    return;
}
function actualizarBarraProgreso() {
    var porcentaje = 0;
    var intervalo = setInterval(function() {
    porcentaje += 100 / 8; 
    $('#barraProgreso').css('width', porcentaje + '%').attr('aria-valuenow', porcentaje);
        if (porcentaje >= 100) clearInterval(intervalo);
    }, 1000);
    }


    function hacerpingelemento(ippe, ipcpe, mac, vlan, vrf, pais, dbcpe) {
        $('#resultadoModal').modal('show');
        $('#barraProgreso').css('width', '0%').attr('aria-valuenow', 0);
        actualizarBarraProgreso(); 
        var url = 'pingdesdepevpn/' + ippe + '/' + ipcpe + '/' + mac + '/' + vlan + '/' + vrf + '/' + pais + '/' + dbcpe + '/';
        $.ajax({
            type: 'POST',
            url: url,
            headers: { 'X-CSRFToken': $('input[name="csrfmiddlewaretoken"]').val() },
            data: { ippe: ippe, ipcpe: ipcpe, mac: mac, vlan: vlan, vrf: vrf, pais: pais, dbcpe: dbcpe },
            success: function(response) {
                $('#barraProgreso').css('width', '100%').attr('aria-valuenow', 100);
                if(response && response.res_ping) {
                    $('#resultadoPing').text(response.res_ping);
                } else {
                    $('#resultadoPing').text('No se pudo obtener el resultado del ping.');
                }
                setTimeout(function() {
                    $('#barraProgreso').parent().hide();
                    }, 500);
                },
            error: function(xhr, status, error) {
                $('#resultadoPing').text('No se pudo obtener el resultado del ping. '+xhr+"-"+status+"-"+"Error:"+error);
            }
            });
        }

  function verdetalleinterface(ipdis, mac, vlan, interface, dbsw) {
    var selectBox = document.getElementById("selectdb");
    var dbdetalle =selectBox.options[0].value;
    //var url = 'detalleinterface/' + ipdis + '/' + mac + '/' + vlan + '/' + vlan + '/' + vrf + '/' + pais + '/' + dbdetalle + '/';
    $.ajax({
      type: 'POST',
      url: url,
      headers: { 'X-CSRFToken': $('input[name="csrfmiddlewaretoken"]').val() },
      data: { ipdis: ipdis, mac: mac, vlan: vlan, interface: interface, bdetalle: dbsw},
      success: function(response) { alert(response.detallainter); },
      error: function(xhr, status, error) { alert('Resultado: ' + error); console.error('Error', error); }
    });
  }