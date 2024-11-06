
function onloadpagewelcome() {  //en welcome
    var selectBox = document.getElementById("selectdbwel");
    var elementoplace =selectBox.options[0].value;
    document.getElementById("iddbselectedwel").value = elementoplace; 
    return;
}

function onloadpagbuscaips() {  //en buscar ips s
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

function onloadpagecasoact() { 
    var selectBoxact = document.getElementById("estadoact");
    var elementoact =selectBoxact.options[0].value;
    document.getElementById("idestadoact").value = elementoact;
    return;
}

function onloadpagecasosr() { 
    var selectBoxsr = document.getElementById("estadosr");
    var elementosr =selectBoxsr.options[0].value;
    document.getElementById("idestadosr").value = elementosr; 
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

function copiaselectestadosr(){ 
    var selectedValue = document.getElementById('estadosr').value;
    document.getElementById('idestadosr').value = selectedValue;
    return;
}

function copiaselectestadoact(){ 
    var selectedValue = document.getElementById('estadoact').value;
    document.getElementById('idestadoact').value = selectedValue;
    return;
}


function agregafechahora() { 
    const fechaActual = new Date();
    const dia = fechaActual.getDate();
    const mes = fechaActual.getMonth() + 1;  
    const año = fechaActual.getFullYear();
    const hora = fechaActual.getHours();
    const minutos = fechaActual.getMinutes().toString().padStart(2, "0"); 
    document.getElementById("idfechaactgra").value = `${dia}/${mes}/${año} ${hora}:${minutos} `;
    document.getElementById("idfechahorasr").value = `${dia}/${mes}/${año} ${hora}:${minutos} `;
    document.getElementById("idusuariomodifica").value = `${dia}/${mes}/${año} ${hora}:${minutos} `;
    return;
}

function agregafechahorasract() { 
    const fechaActual = new Date();
    const dia = fechaActual.getDate();
    const mes = fechaActual.getMonth() + 1;  
    const año = fechaActual.getFullYear();
    document.getElementById("idfechaactgra").value = `${dia}/${mes}/${año} ${hora}:${minutos} `;
    document.getElementById("idfechahorasr").value = `${dia}/${mes}/${año} ${hora}:${minutos} `;
    document.getElementById("idusuariomodifica").value = `${dia}/${mes}/${año} ${hora}:${minutos} `;
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
    barraProgreso.parent().addClass('your-class-style').css('margin-top', '20px').show();
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

//------------------------------------------------------------------------------------------------------------------------
$(document).on('click', 'button[id^="btn-"]', function() {
    var idParts = this.id.split('-');
    var dbsw = idParts[1];
    var ipdis = idParts[2];
    var interface = idParts[3];
    verdetalleinterface(dbsw, ipdis, interface);
});
//----------------------------------------------------------------------------------------------------------------------


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
    .sch(function(error) {
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



//GENERAR MODAL ACTIVIDAD

function actualizaract(registroact, codigoact, vendoract, estadoact) {
    const fechaActual = new Date();
    const dia = fechaActual.getDate();
    const mes = fechaActual.getMonth() + 1;  
    const año = fechaActual.getFullYear();
    const hora = fechaActual.getHours();
    const minutos = fechaActual.getMinutes().toString().padStart(2, "0");
    const grabacion = `${dia}/${mes}/${año} ${hora}:${minutos}`;
    
    var url = '/actualizarmodales/'; 

    $.ajax({
        url: url,
        type: 'POST',
        beforeSend: function(xhr) {
            xhr.setRequestHeader("X-CSRFToken", $('input[name="csrfmiddlewaretoken"]').val());
        },
        success: function(response) {
            var vendors = response.vendors || [];
            var estados = response.estados || [];
            var modalHtml = `
                <div class="modal fade" id="exampleModalact" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
                    <div class="modal-dialog">
                        <div class="modal-content">
                            <div class="modal-header">
                                <h5 class="modal-title" id="exampleModalLabel">Administrar actividad no:  ${codigoact}</h5>
                                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                            </div>
                            <div class="modal-body">
                                <form >
                                    <fieldset>

                                        <div class="form-group">
                                            <span id="idregistroactdblay" name="idregistroactdblay">Registro: </span>
                                            <span id="idregistroactdb" name="idregistroactdb">${registroact}</span>
                                        </div>

                                        <div class="form-group">
                                            <span id="idfechahoraactactmolay" name="idfechahoraactactmolay">Fecha  Hora: </span>
                                            <span id="idfechahoraactactmo" name="idfechahoraactactmo">${grabacion}</span>
                                        </div>

                                        <div class="form-group">
                                            <span id="idusuariomodificaactmodlay" name="idusuariomodificaactmodlay">Usuario: </span>
                                            <span id="idusuariomodificaactmod" name="idusuariomodificaactmod">navalos</span>
                                        </div>
                                        
                                        <div class="form-group">
                                            &nbsp&nbsp&nbsp&nbsp
                                            <textarea class="form-control" id="idinfoactualizacionactmod" name="idinfoactualizacionactmod" placeholder="Actualización" rows="3" maxlength="195" oninput="this.value = this.value.substring(0, this.maxLength)" required maxlength="195"></textarea>
                                        </div>

                                        <div class="form-group">
                                            &nbsp&nbsp&nbsp&nbsp
                                            <div class="row">

                                                <div class="col-md-4">
                                                    <select id="idvendoractmod" name="idvendoractmod" class="form-select">
                                                        ${vendors.map(v => `<option value="${v}" ${v === vendoract ? 'selected' : ''}>${v}</option>`).join('')}
                                                    </select>
                                                </div>

                                                <div class="col-md-4">
                                                    <select id="estadoactmod" name="estadoactmod" class="form-select">
                                                        ${estados.map(e => `<option value="${e}" ${e === estadoact ? 'selected' : ''}>${e}</option>`).join('')}
                                                    </select>
                                                </div>

                                                 <div class="col-md-4">
                                                    <input class="form-control" id="idestadoactac" type="text" name="idestadoactac" readonly="" value="${estadoact}">
                                                </div>
                                                                                            
                                            </div>
                                        </div>
                                    </fieldset>
                                </form>

                                <div class="modal-footer" style="margin-top: 10px;" >
                                    <button id="idopcionesact" type="button" class="btn btn-primary" onclick="actualizacionactmodal(); return false;">
                                        Actualizar
                                    </button>
                                </div>

                            </div>
                        </div>
                    </div>
                </div>
            `;

            $('body').append(modalHtml);
            $('#exampleModalact').modal('show');
            $('#exampleModalact').on('hidden.bs.modal', function () {
                $(this).remove();
            });
        },
        error: function(xhr, status, error) {
            alert('Error: ' + error);
        }
    });
}


function actualizacionactmodal() {
    // Obtener los valores desde el DOM
    var registroact = document.getElementById('idregistroactdb').textContent;
    var fechamodal = document.getElementById('idfechahoraactactmo').textContent;
    var fechaactmodal = toHexString(fechamodal);  // Convertir fecha a hex
    var actualizacion = sanitizeString(document.getElementById('idinfoactualizacionactmod').value);
    var usuarioact = document.getElementById('idusuariomodificaactmod').textContent;
    var estadoact = document.getElementById('estadoactmod').value;
    var vendoract = document.getElementById('idvendoractmod').value;

    // Validación: Verificar que el campo 'actualizacion' no esté vacío
    if (actualizacion.trim() === "") {
        alert("Por favor, ingrese una actualización antes de guardar.");
        return;  // Detener la ejecución si no hay actualización
    }

    // Generar la URL con encodeURIComponent para asegurar que los valores sean válidos en la URL
    var url = 'actualizacionact/' + encodeURIComponent(registroact) +
                              '/' + encodeURIComponent(fechaactmodal) +
                              '/' + encodeURIComponent(actualizacion) +
                              '/' + encodeURIComponent(usuarioact) +
                              '/' + encodeURIComponent(estadoact) +
                              '/' + encodeURIComponent(vendoract) + '/';

    // Confirmación antes de enviar los cambios
    var confirmar = confirm("¿Desea grabar los cambios?");

    if (confirmar) {
        $.ajax({
            url: url,
            type: 'POST',
            beforeSend: function(xhr) {
                xhr.setRequestHeader("X-CSRFToken", $('input[name="csrfmiddlewaretoken"]').val());
            },
            success: function(response) {
                alert('Los cambios se han grabado exitosamente.');
                $('#exampleModalact').modal('hide');
                $('#exampleModalact').on('hidden.bs.modal', function () {
                    $(this).remove();
                    location.reload();
                });
            },
            error: function(xhr, status, error) {
                alert('Error: ' + error);
            }
        });
    } else {
        alert('La grabación ha sido cancelada.');
    }
}


function actualizarsr(registrosractividadsr, codigosr, vendorsr, estadosr, paisNombresr) {
    const fechaActual = new Date();
    const dia = fechaActual.getDate();
    const mes = fechaActual.getMonth() + 1;  
    const año = fechaActual.getFullYear();
    const hora = fechaActual.getHours();
    const minutos = fechaActual.getMinutes().toString().padStart(2, "0");
    const grabacion = `${dia}/${mes}/${año} ${hora}:${minutos}`;
    let paissr;

    switch (paisNombresr) {
        case 'GT':
            paissr = 'GUATEMALA';
            break;
        case 'HN':
            paissr = 'HONDURAS';
            break;
        case 'SV':
            paissr = 'EL SALVADOR';
            break;
        case 'CR':
            paissr = 'COSTA RICA';
            break;
        case 'NI':
            paissr = 'NICARAGUA';
            break;
        default:
            paissr = 'País no reconocido';
    }

    var url = '/actualizarmodales/';  

    $.ajax({
        url: url,
        type: 'POST',
        beforeSend: function(xhr) {
        xhr.setRequestHeader("X-CSRFToken", $('input[name="csrfmiddlewaretoken"]').val());
    },
    success: function(response) {
        var vendors = response.vendors || [];
        var estados = response.estados || [];
        var paises = response.paises || [];
        var modalHtml = `
        <div class="modal fade" id="exampleModalsr" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title" id="exampleModalLabel">Administrar Caso #:  ${codigosr}</h5>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        <form >
                            <fieldset>
                                <div class="form-group">
                                    <span id="idregistrosrdbly" name="idregistrosrdbly">Registro: </span>
                                    <span id="idregistrosrdb" name="idregistrosrdb">${registrosractividadsr}</span>    
                                </div>

                                <div class="form-group">
                                    <span id="idfechahoraactsrmoly" name="idfechahoraactsrmoly">Fecha  Hora: </span>
                                    <span id="idfechahoraactsrmo" name="idfechahoraactsrmo">${grabacion}</span>
                                </div>

                                <div class="form-group">
                                    <span id="idusuariomodificasrmodly" name="idusuariomodificasrmodly">Usuario: </span>
                                    <span id="idusuariomodificasrmod" name="idusuariomodificasrmod">navalos</span>
                                </div>

                                 <div class="form-group">
                                    &nbsp&nbsp&nbsp&nbsp
                                    <input type="text" class="form-control" id="idsrrmamod" name="idsrrmamod" placeholder="No. RMA ..." >
                                 </div>

                                 <div class="form-group">
                                    &nbsp&nbsp&nbsp&nbsp
                                    <input type="text" class="form-control" id="idsrttmod" name="idsrttmod" placeholder="Dato adicional ..." >
                                 </div>

                                 <div class="form-group">
                                    &nbsp&nbsp&nbsp&nbsp
                                    <input type="text" class="form-control" id="idsrttmodfecharma" name="idsrttmodfecharma" placeholder="Fecha-Hora Entrega RMA ..." >
                                 </div>
                                
                                <div class="form-group">
                                    &nbsp&nbsp&nbsp&nbsp
                                    <textarea class="form-control" id="idinfoactualizacionsrmod" name="idinfoactualizacionsrmod" placeholder="Actualización" rows="3" maxlength="200" oninput="this.value = this.value.substring(0, this.maxLength)"required maxlength="180"></textarea>
                                </div>

                                <div class="form-group">
                                    <div class="row">
                                        <div class="col-md-4">
                                         &nbsp&nbsp&nbsp&nbsp
                                            <input class="form-control" id="idvendorsrmodac" type="text" name="idvendorsrmodac" readonly="" value="${vendorsr}">
                                        </div>

                                        <div class="col-md-4">
                                         &nbsp&nbsp&nbsp&nbsp
                                            <input class="form-control" id="idestadosrmodac" type="text" name="idestadosrmodac" readonly="" value="${estadosr}">
                                        </div>

                                        <div class="col-md-4">
                                         &nbsp&nbsp&nbsp&nbsp
                                            <input class="form-control" id="idepaissrmodac" type="text" name="idepaissrmodac" readonly="" value="${paissr}">
                                        </div>
                                    </div>
                                </div>

                                <div class="form-group">
                                    &nbsp&nbsp&nbsp&nbsp    
                                    <div class="row">
                                        <div class="col-md-4">
                                            <select id="idvendorsrmod" name="idvendorsrmod" class="form-select">
                                                ${vendors.map(v => `<option value="${v}" ${v === vendorsr ? 'selected' : ''}>${v}</option>`).join('')}
                                            </select>
                                        </div>

                                        <div class="col-md-4">
                                            <select id="estadosrmod" name="estadosrmod" class="form-select">
                                                ${estados.map(e => `<option value="${e}" ${e === estadosr ? 'selected' : ''}>${e}</option>`).join('')}
                                            </select>
                                        </div>

                                         <div class="col-md-4">
                                            <select id="paissrmod" name="paissrmod" class="form-select">
                                                ${paises.map(i => `<option value="${i}" ${i === paissr ? 'selected' : ''}>${i}</option>`).join('')}
                                            </select>
                                        </div>

                                    </div>
                                </div>
                            </fieldset>
                        </form>

                        <div class="modal-footer" style="margin-top: 10px;" >
                            <button id="idopcionessrr" type="button" class="btn btn-primary" onclick="actualizacionsrmodal(); return false;">
                                Actualizar
                            </button>
                        </div>

                    </div>
                </div>
            </div>
        </div>
    `;

    $('body').append(modalHtml);
    $('#exampleModalsr').modal('show');
    $('#exampleModalsr').on('hidden.bs.modal', function () {
                $(this).remove();
            });
        },
        error: function(xhr, status, error) {
            alert('Error: ' + error);
        }
    });
}

function actualizacionsrmodal() {
    var registrosr = document.getElementById('idregistrosrdb').textContent;
    var fechahoragrabacion = toHexString(document.getElementById('idfechahoraactsrmo').textContent);
    var rmarecibido = document.getElementById('idsrrmamod').value;
    var ttrmarecibido = document.getElementById('idsrttmod').value;
    var fecharmasrrecibida = document.getElementById('idsrttmodfecharma').value;
    var actualizacion = document.getElementById('idinfoactualizacionsrmod').value;
    var usuariosr = document.getElementById('idusuariomodificasrmod').textContent;
    var estadosr = document.getElementById('estadosrmod').value;
    var vendorsr = document.getElementById('idvendorsrmod').value;
    var paissr = document.getElementById('paissrmod').value;

    if (rmarecibido.trim() === "") {
        rma = "0";
    } else {
        rma = sanitizeString(rmarecibido);
    }
    
    if (ttrmarecibido.trim() === "") {
        ttrma = "0";
    } else {
        ttrma = sanitizeString(ttrmarecibido);
    }
    
    if (fecharmasrrecibida.trim() === "") {
        fecharmasr = toHexString("sin_fecha");
    } else {
        fecharmasr_ = sanitizeString(fecharmasrrecibida);
        fecharmasr = toHexString(fecharmasr_);

    }
    
    if (actualizacion.trim() === "") {
        actualizacion = "sin_act";
    } else {
        actualizacion = sanitizeString(actualizacion);
    }
    
    alert(rma);
    var url = 'actualizacionsr/' + 
    encodeURIComponent(registrosr) + '/' +
    encodeURIComponent(fechahoragrabacion) + '/' +
    encodeURIComponent(rma) + '/' +
    encodeURIComponent(ttrma) + '/' +
    encodeURIComponent(fecharmasr) + '/' +
    encodeURIComponent(actualizacion) + '/' +
    encodeURIComponent(usuariosr) + '/' +
    encodeURIComponent(estadosr) + '/' +
    encodeURIComponent(vendorsr) + '/' +
    encodeURIComponent(paissr) + '/'; 
    
    var confirmar = confirm("¿Desea grabar los cambios?");

    if (confirmar) {
        $.ajax({
            url: url,
            type: 'POST',
            beforeSend: function(xhr) {
                xhr.setRequestHeader("X-CSRFToken", $('input[name="csrfmiddlewaretoken"]').val());
            },
            success: function(response) {
                alert('Los cambios se han grabado exitosamente.');
                $('#exampleModalsr').modal('hide');
                $('#exampleModalsr').on('hidden.bs.modal', function () {
                    $(this).remove();
                    location.reload();
                });
            },
            error: function(xhr, status, error) {
                alert('Error: ' + error);
            }
        });
    } else {
        alert('La grabación ha sido cancelada.');
    }
}




function mostrarInformacionDescripcion(descripcion) {
    alert('Descripción:  ' + descripcion);
    return false;
  }

function mostrarInformacionDetalle(detalle) {
    alert('Detalle: ' + detalle );
    return false;
}

function mostrarInformacionfechacrea(fechacreacioncaso, usuario) {
    alert('Fecha Apertura: '+fechacreacioncaso + ' Por: ' + usuario);
    return false;
}

function mostrarInformacionRMAS(registro, fechagrab, ttrma, actualizacion, fechaentrega, usuariomodifica) {
    alert('Detalle: ' + registro + ' Fecha Grabación: ' + fechagrab + 
        ' TTRMA: ' + ttrma + ' Actualización: ' + actualizacion + 
        ' Fecha Entrega: ' + fechaentrega + ' Usuario: ' + usuariomodifica);
    return false;
  }

  function mostrarActualizacionesAct(registro) {
    var url = '/actualizacionactividades/' + registro + '/'; 
    $.ajax({
        url: url,
        type: 'POST',
        beforeSend: function(xhr) {
            xhr.setRequestHeader("X-CSRFToken", $('input[name="csrfmiddlewaretoken"]').val());
        },
        success: function(response) {
            var lista = response.listaactualizacionactividad;
            var mensaje = "Actualizaciones:\n";
            lista.forEach(function(item) {
                mensaje += "ID: " + item.idregistro + ", Fecha: " + item.fechahoragrabacion + ", Actualización: " + item.actualizacion + ", Usuario: " + item.usuariomodifica + "\n";
            });

            alert(mensaje);
        },
        error: function(xhr, status, error) {
            alert('Error: ' + error);
        }
    }); 
    return false;
}

function confirmarYEnviarsr() {
    var confirmar = confirm("¿Desea guardar los cambios?");
    if (confirmar) {
        document.getElementById('idformagregaract').submit();
        location.reload();
    } else {
        alert('La acción ha sido cancelada.');
    }
}

function confirmarYEnviaract() {
    var confirmar = confirm("¿Desea guardar los cambios?");
    if (confirmar) {
        document.getElementById('idformagregarsr').submit();
        location.reload();
    } else {
        alert('La acción ha sido cancelada.');
    }
}


function sanitizeString(str) {
    str = str.replace(/[\/\?&=#%]/g, '_');  // Reemplazar caracteres problemáticos con '_'
    str = str.replace(/\t/g, ' ');  // Reemplazar tabuladores por espacios
    str = str.trim();  // Elimina espacios en blanco al principio y final de la cadena
    return str || 'sin_dato';  // Si la cadena está vacía, devolver 'sin_dato'
}




//--------------------------------- GRAFICOS --------------------------------------------//
function diagramal2() {
    fetch('/about/diagramal2/')
    .then(response => response.json())
    .then(data => {
    var svgWidth = 700;
    var svgHeight = 400;
    
    var svg = d3.select("#vis-red").append("svg")
    .attr("width", svgWidth)
    .attr("height", svgHeight);
    
    var simulation = d3.forceSimulation(data.nodes)
    .force("link", d3.forceLink(data.links).id(d => d.id).distance(100))
    .force("charge", d3.forceManyBody().strength(-200))
    .force("center", d3.forceCenter(svgWidth / 2, svgHeight / 2));
    
    var links = svg.selectAll(".link")
    .data(data.links)
    .enter().append("line")
    .attr("class", "link")
    .style("stroke", "#999")
    .style("stroke-opacity", 0.6)
    .style("stroke-width", 4);
    
    var nodes = svg.selectAll(".node")
    .data(data.nodes)
    .enter().append("image")
    .attr("class", "node")
    .attr("xlink:href", function(d) { 
    return "/static/img/" + d.tipo + ".png"; 
    })
    .attr("width", 60)
    .attr("height", 60)
    .call(d3.drag()
    .on("start", dragstarted)
    .on("drag", dragged)
    .on("end", dragended));

    
    simulation.on("tick", () => {
    links.attr("x1", d => d.source.x)
    .attr("y1", d => d.source.y)
    .attr("x2", d => d.target.x)
    .attr("y2", d => d.target.y);

    nodes.attr("x", d => d.x - 15)
    .attr("y", d => d.y - 15);
    });
    
    function dragstarted(d) {
    if (!d3.event.active) simulation.alphaTarget(0.3).restart();
    d.fx = d.x;
    d.fy = d.y;
    }
    
    function dragged(d) {
    d.fx = d3.event.x;
    d.fy = d3.event.y;
    }
    
    function dragended(d) {
    if (!d3.event.active) simulation.alphaTarget(0);
    d.fx = null;
    d.fy = null;
    }
    })
    .catch(error => console.error('Error:', error));
    }