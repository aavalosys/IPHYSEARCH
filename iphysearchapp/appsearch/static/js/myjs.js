
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

function onloadpageimpacto() { 
    var selectBox = document.getElementById("selectdb");
    var elementoplace =selectBox.options[0].value;
    document.getElementById("idtxtdb").value = elementoplace; 
    return;
}
function onloadpagesaturaciones() { 
    var selectBox = document.getElementById("selectdb");
    var elementoplace =selectBox.options[0].value;
    document.getElementById("idtxtdb").value = elementoplace; 
    return;
}

function onloadpagesgraficas() { 
    var selectBox = document.getElementById("selectdb");
    var elementoplace =selectBox.options[0].value;
    document.getElementById("idtxtdb").value = elementoplace; 
    return;
}

function onloadpagevarios() { 
    var selectBox = document.getElementById("selectdb");
    var elementoplace =selectBox.options[0].value;
    document.getElementById("idtxtdb").value = elementoplace; 
    return;
}

function onloadpagesmantenimiento() { 
    var tituloIps = document.getElementById("mantenimiento");
    tituloIps.classList.add("font-weight-bold", "text-white");
    return;
}

function onloadpagesabout() { 
    var tituloIps = document.getElementById("about");
    tituloIps.classList.add("font-weight-bold", "text-white");
    return;
}

function copiaripnodo(ipnodo) { 
    document.getElementById("idtxtip").value = ipnodo;
    return;
}

function copiaselectdbs(){ 
    var selectedValue = document.getElementById('selectdbwel').value;
    document.getElementById('iddbselectedwel').value = selectedValue;
    return;
}

function copiaselectdbsrbs(){ 
    var selectedValue = document.getElementById('selectdb').value;
    document.getElementById('dbrbs').value = selectedValue;
    return;
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
    return;
}

function hacerpingelemento(ippe, ipcpe, vrf) {
    var barraProgreso = $('#barraProgreso');
    $('#resultadoPing').text('');
    $('#resultadoModal').modal('show');
    barraProgreso.css('width', '0%').attr('aria-valuenow', 0);
    barraProgreso.parent().show();
    barraProgreso[0].offsetHeight; 
    actualizarBarraProgreso();
    actualizarCSRFToken();

        $(document).on('click', '#Pingbtn', function() {
            var url = 'pingdesdepevpn/' + ippe + '/' + ipcpe + '/' + vrf + '/';
            $.ajax({
            type: 'POST',
            url: url,
            cache: false,
            data: { ippe: ippe, ipcpe: ipcpe, vrf: vrf },
                success: function(response) {
                barraProgreso.css('width', '100%').attr('aria-valuenow', 100);
                if(response) {
                    $('#resultadoPing').text(response.res_ping);
                } else {
                    $('#resultadoPing').text('No se pudo obtener el resultado del ping.');
                }
                setTimeout(function() { barraProgreso.parent().hide(); }, 500);
                },
                error: function(xhr, status, error) {
                    $('#resultadoPing').text('Error en ping: ' + xhr + "----" + status + "-" + "Error:" + error );
                }
            });
        });
    return;
} 

function listar_tabla_mac(ip0, ip1, ip2, ip3, ip4, ip5, ip6, ip7) {
    var url = 'buscar_macajax/' + ip0 + '/' + ip1 + '/' + ip2 + '/' + ip3 + '/' + ip4 + '/' + ip5 + '/' + ip6 + '/' + ip7 + '/';
    $.ajax({
        type: 'GET',
        url: url,
        cache: false,
        data: { ip0: ip0, ip1: ip1, ip2: ip2, ip3: ip3, ip4: ip4, ip5: ip5, ip6: ip6, ip7: ip7 },
        success: function(response) {
            var table = $('#tablamac');
            table.empty();
            var headers = ['ESTADO', 'DISPOSITIVO', 'MAC', 'VLAN-PW', 'INTERFACE/PEER', 'DETALLE', '#MAC', 'DESCRIPCIÓN'];
            var thead = $('<thead></thead>');
            var tr = $('<tr></tr>');
            for (var i = 0; i < headers.length; i++) {
                var th = $('<th></th>').text(headers[i]);
                tr.append(th);
            }
            thead.append(tr);
            table.append(thead);
            var tbody = $('<tbody></tbody>').attr('id', 'tablamac-body');
            $.each(response.listar_mac, function(i, equipo) {
                var clase = equipo[6] === 'Up' ? 'table-success' : 'table-danger';
                var fila = '<tr class="' + clase + '">' +
                                '<td width="30">' + equipo[6] + '</td>' +
                                '<td width="80">' + equipo[0] + '</td>' +
                                '<td width="100">' + equipo[1] + '</td>' +
                                '<td width="100">' + equipo[2] + '</td>' +
                                '<td width="100">' + equipo[3] + '</td>' +
                                '<td width="100">' +
                                    '<button type="button" id="btn-' + equipo[3] + '" class="btn btn-info" onclick="verdetalleinterface(\'' + equipo[2] + '\', \'' + equipo[0] + '\', \'' + equipo[3] + '\'); return false;">&#x1F50E</button>' +
                                '</td>' +
                                '<td width="30">' + equipo[4] + '</td>' +
                                '<td width="30">' + equipo[5] + '</td>' +
                            '</tr>';
                tbody.append(fila);
            });
            table.append(tbody);
        },
        error: function(xhr, status, error) {
            console.error('Error al listar la tabla MAC:', error);
        }
    });
    return;
}

function verdetalleinterface(dbsw, ipdis, interface) {
    console.log('dbsw:', dbsw);
    console.log('ipdis:', ipdis);
    console.log('interface:', interface);
    
    var barraProgreso = $('#barraProgresodetalle');
    dbsw = "fy2024w19";
    interface = toHexString(interface);
    var url = 'detalleinterface/' + dbsw + '/' + ipdis + '/' + interface + '/';
    $('#detalleInterface').text('');
    $('#resultadoModalinterface').modal('show');
    barraProgreso.css('width', '0%').attr('aria-valuenow', 0);
    barraProgreso.parent().show();
    barraProgreso[0].offsetHeight;
    actualizarBarraProgresodetalle();
    actualizarCSRFToken();
    
    $.ajax({
        type: 'POST',
        url: url,
        cache: false,
        data: { dbsw: dbsw, ipdis: ipdis, interface: interface },
        success: function(response) {
            barraProgreso.css('width', '100%').attr('aria-valuenow', 100);
            if(response) {
                $('#detalleInterface').text(response.detalleInterface);
            } else {
                $('#detalleInterface').text('Error al interrogar la interface');
            }
            setTimeout(function() { barraProgreso.parent().hide(); }, 500);
            },
        error: function(xhr, status, error) {
            $('#detalleInterface').text('Detalle del Error: ' + xhr + "----" + status + "-" + "Error:" + error );
        }
    });
}

$(document).on('click', 'button[id^="btn-"]', function() {
    var idParts = this.id.split('-');
    var dbsw = idParts[1];
    var ipdis = idParts[2];
    var interface = idParts[3];
    verdetalleinterface(dbsw, ipdis, interface);
});

function actualizarBarraProgresodetalle() {
    var porcentaje = 0;
    var intervalo = setInterval(function() {
    porcentaje += 100 / 5; 
    $('#barraProgresodetalle').css('width', porcentaje + '%').attr('aria-valuenow', porcentaje);
        if (porcentaje >= 100) clearInterval(intervalo);
    }, 1000);
    return;
}

function toHexString(characters) {
    return characters.split('').map(function(char) {
    return char.charCodeAt(0).toString(16);
    }).join('');
    return;
}

function actualizarCSRFToken() {
    var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    $.ajaxSetup({
    headers: { 'X-CSRFToken': csrfToken }
    });
    return;
}

function copiarAlPortapapeles() {
    var texto = document.getElementById('resultadoPing').innerText;
    navigator.clipboard.writeText(texto).then(function() {
    console.log('Texto copiado al portapapeles');
    })
    .catch(function(error) {
    console.error('Error al copiar texto: ', error);
    });
    return;
}

function copiarAlPortapapelesdetalle() {
    var texto = document.getElementById('detalleInterface').innerText;
    navigator.clipboard.writeText(texto).then(function() {
    console.log('Texto copiado al portapapeles');
    })
    .catch(function(error) {
    console.error('Error al copiar texto: ', error);
    });
    return;
}

