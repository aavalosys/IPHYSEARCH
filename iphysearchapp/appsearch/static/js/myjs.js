
function onloadpagewelcome() {  //en welcome
    var selectBox = document.getElementById("selectdbwel");
    var elementoplace =selectBox.options[0].value;
    document.getElementById("iddbselectedwel").value = elementoplace; 
    return;
}

function copiaselectdbsbackup() { //en welcome
    var selecteddbbaciup = document.getElementById("selectdbwel").value;
    document.getElementById("iddbselectedwel").value = selecteddbbaciup; 
    return;
}

function onloadpagbuscaips() {  //en buscar ipss
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
    return;
}

function agregafechahorasr() { 
    const fechaActual = new Date();
    const dia = fechaActual.getDate();
    const mes = fechaActual.getMonth() + 1;  
    const año = fechaActual.getFullYear();
    const hora = fechaActual.getHours();
    const minutos = fechaActual.getMinutes().toString().padStart(2, "0"); 
    document.getElementById("idfechahorasr").value = `${dia}/${mes}/${año} ${hora}:${minutos} `;
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


function actualizaract(registroact, codigoact, vendoract, estadoact, username) { 
    const fechaActual = new Date();
    const dia = fechaActual.getDate();
    const mes = fechaActual.getMonth() + 1;  
    const año = fechaActual.getFullYear();
    const hora = fechaActual.getHours();
    const minutos = fechaActual.getMinutes().toString().padStart(2, "0");
    const grabacion = `${dia}/${mes}/${año} ${hora}:${minutos}`;
    var url = 'obtiene_vendors_estados/'; 
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
                                            <span id="idfechahoraactactmolay" name="idfechahoraactactmolay">Fecha-Hora Actual: </span>
                                            <span id="idfechahoraactactmo" name="idfechahoraactactmo">${grabacion}</span>
                                        </div>

                                        <div class="form-group">
                                            <span id="idusuariomodificaactmodlay" name="idusuariomodificaactmodlay">Usuario: </span>
                                            <span id="idusuariomodificaactmod" name="idusuariomodificaactmod">${username}</span>
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
                location.reload();
            });
        },
        error: function(xhr, status, error) {
            alert('Error: ' + error);
        }
    });
}


function actualizacionactmodal() {
    var registroact = document.getElementById('idregistroactdb').textContent;
    var fechamodal = document.getElementById('idfechahoraactactmo').textContent;
    var fechaactmodal = toHexString(fechamodal);  
    var actualizacion = sanitizeString(document.getElementById('idinfoactualizacionactmod').value);
    var usuarioact = document.getElementById('idusuariomodificaactmod').textContent;
    var estadoact = document.getElementById('estadoactmod').value;
    var vendoract = document.getElementById('idvendoractmod').value;

    if (actualizacion.trim() === "") {
        alert("Ingrese una actualización antes de guardar.");
        return;  
    }
    var pageNumber = getPageNumberFromURLact();
    var url = '/agregar_act/actividades/' + encodeURIComponent(pageNumber) +
              '/actualizacionact/' + encodeURIComponent(registroact) +
              '/' + encodeURIComponent(fechaactmodal) +
              '/' + encodeURIComponent(actualizacion) +
              '/' + encodeURIComponent(usuarioact) +
              '/' + encodeURIComponent(estadoact) +
              '/' + encodeURIComponent(vendoract) + '/';

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
                    window.location.reload();
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

function getPageNumberFromURLact() {
    var currentURL = window.location.href;
    var pageNumberMatch = currentURL.match(/\/agregar_act\/(\d+)\//); // Cambia la expresión regular para el nuevo formato
    return pageNumberMatch ? pageNumberMatch[1] : 0; // Si no se encuentra, asumimos la página 0
}

function getPageNumberFromURLsr() {
    var currentURL = window.location.href;
    var pageNumberMatch = currentURL.match(/\/agregar_sr\/(\d+)\//); // Cambia la expresión regular para el nuevo formato
    return pageNumberMatch ? pageNumberMatch[1] : 0; // Si no se encuentra, asumimos la página 0
}



//GENERAR MODAL ACTIVIDAD
function actualizarsr(registrosractividadsr, codigosr, vendorsr, estadosr, paisNombresr, username) {
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

    var url = 'obtiene_proveedores_estados_paises/';  
    $.ajax({
        url: url,
        type: 'POST',
        beforeSend: function(xhr) {
            xhr.setRequestHeader("X-CSRFToken", $('input[name="csrfmiddlewaretoken"]').val());
        },
        success: function(response) {
            var proveedores = response.proveedores || [];
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
                            <form>
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
                                        <span id="idusuariomodificasrmod" name="idusuariomodificasrmod">${username}</span>
                                        &nbsp;&nbsp;&nbsp;&nbsp;
                                        &nbsp;&nbsp;&nbsp;&nbsp;
                                    </div>

                                    <div class="form-group">
                                        <button id="btnActualizacion" type="button" class="btn btn-info" 
                                            onclick="toggleActualizacion();">
                                            Actualización
                                        </button>
                                    </div>

                                    <!-- Campo RMA -->
                                    <div class="form-group">
                                    &nbsp&nbsp&nbsp&nbsp;
                                        <input type="text" class="form-control" id="idsrrmamod" name="idsrrmamod" placeholder="No. RMA ..." > <!-- RMA -->
                                    </div>

                                    <!-- Campo adicional -->
                                    <div class="form-group">
                                    &nbsp&nbsp&nbsp&nbsp
                                        <input type="text" class="form-control" id="idsrttmod" name="idsrttmod" placeholder="ITEM ..." > <!-- ITEM -->
                                    </div>

                                    <!-- Campo fecha -->
                                    <div class="form-group">
                                    &nbsp&nbsp&nbsp&nbsp
                                        <input type="date" class="form-control" id="idfechasropen" name="idfechasropen" placeholder="Fecha apertura" required>
                                        <small id="emailHelp2" class="form-text text-muted">Fecha de apertura RMA</small>
                                    </div>
                                    
                                    <!-- Campo Actualización -->
                                    <div class="form-group">
                                    &nbsp&nbsp&nbsp&nbsp
                                        <textarea class="form-control" id="idinfoactualizacionsrmod" name="idinfoactualizacionsrmod" 
                                            placeholder="Actualización" rows="3" maxlength="200" oninput="this.value = this.value.substring(0, this.maxLength)" required></textarea>
                                    </div>

                                    <div class="form-group">
                                    &nbsp&nbsp&nbsp&nbsp
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
                                                ${proveedores.map(v => `<option value="${v}" ${v === vendorsr ? 'selected' : ''}>${v}</option>`).join('')}
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

                            <div class="modal-footer">
                                <button id="idopcionessrr" type="button" class="btn btn-primary" onclick="actualizacionsrmodal(); return false;">
                                    Guardar
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
                location.reload();
            });
        },
        error: function(xhr, status, error) {
            alert('Error: ' + error);
        }
    });
}


function toggleActualizacion() {
    const campoRMA = document.getElementById('idsrrmamod');
    const campoAdicional = document.getElementById('idsrttmod');
    const campoFecha = document.getElementById('idfechasropen');
    const deshabilitado = campoRMA.disabled;

    campoRMA.disabled = !deshabilitado;
    campoAdicional.disabled = !deshabilitado;
    campoFecha.disabled = !deshabilitado;

    if (!deshabilitado) {
        campoRMA.disabled = false;
        campoAdicional.disabled = false;
        campoFecha.disabled = false;

        campoRMA.value = '0';
        campoAdicional.value = '0';
        campoFecha.value = '00/00/00';
        campoRMA.disabled = true;
        campoAdicional.disabled = true;
        campoFecha.disabled = true;
    }

    const btnActualizacion = document.getElementById('btnActualizacion');
    if (deshabilitado) {
        btnActualizacion.textContent = 'Actvar Actualización';
    } else {
        btnActualizacion.textContent = 'Desactivar Actualización';
    }
}


function actualizacionsrmodal() {
    var registrosr = document.getElementById('idregistrosrdb').textContent;
    var fechahoragrabacion = toHexString(document.getElementById('idfechahoraactsrmo').textContent);
    var rmarecibido = document.getElementById('idsrrmamod').value;
    var ttrmarecibido = document.getElementById('idsrttmod').value;
    var fecharmasrrecibida = document.getElementById('idfechasropen').value;
    var actualizacion = document.getElementById('idinfoactualizacionsrmod').value;
    var usuariosr = document.getElementById('idusuariomodificasrmod').textContent;
    var estadosr = document.getElementById('estadosrmod').value;
    var vendorsr = document.getElementById('idvendorsrmod').value;
    var paissr = document.getElementById('paissrmod').value;

    if (actualizacion.trim() === "") {
        alert('El campo de actualización es obligatorio.');
        return; 
    }

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
        fecharmasr = toHexString("0");
    } else {
        fecharmasr_ = sanitizeString(fecharmasrrecibida);
        fecharmasr = toHexString(fecharmasr_);
    }
    
    if (actualizacion.trim() === "") {
        actualizacion = "sin_act";
    } else {
        actualizacion = sanitizeString(actualizacion);
    }

    var pageNumber = getPageNumberFromURLsr();
    var url = '/agregar_sr/casossr/' + encodeURIComponent(pageNumber) +
              '/actualizacionsr/' +  encodeURIComponent(registrosr) + '/' +
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

function mostrarInformacionDescripcionsr(registro) {
    var url = '/muestradescripcionsr/' + encodeURIComponent(registro) +'/'; 
    $.ajax({
        url: url,
        type: 'GET', 
        beforeSend: function(xhr) {
            xhr.setRequestHeader("X-CSRFToken", $('input[name="csrfmiddlewaretoken"]').val());
        },
        success: function(response) {
            if (response.descripcionSR) {
                alert('Descripción: ' + response.descripcionSR);
            } else {
                alert('No se encontró información para este registro.');
            }
        },
        error: function(xhr, status, error) {
            console.error('Error:', error);
            alert('Ocurrió un error al obtener la descripción');
        }
    }); 
    return false;
}


function mostrarInformacionDescripcionact(registro) {
    var url = '/muestradescripcionact/' + encodeURIComponent(registro) +'/'; 
    $.ajax({
        url: url,
        type: 'GET', 
        beforeSend: function(xhr) {
            xhr.setRequestHeader("X-CSRFToken", $('input[name="csrfmiddlewaretoken"]').val());
        },
        success: function(response) {
            if (response.descripcionACT) {
                alert('Descripción: ' + response.descripcionACT);
            } else {
                alert('No se encontró información para este registro.');
            }
        },
        error: function(xhr, status, error) {
            console.error('Error:', error);
            alert('Ocurrió un error al obtener la descripción');
        }
    }); 
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

function cierreRMAS(registrosractividadsr, codigosr, vendorsr, estadosr, paissr, idregistro, rma, ttrma, actualizacion, fechahoragrabacion, username) {
    const fechaActual = new Date();
    const dia = fechaActual.getDate();
    const mes = fechaActual.getMonth() + 1;
    const año = fechaActual.getFullYear();
    const hora = fechaActual.getHours();
    const minutos = fechaActual.getMinutes().toString().padStart(2, "0");
    const grabacion = `${dia}/${mes}/${año} ${hora}:${minutos}`;

    // Determina si el estado es CLOSED
    const isClosed = estadosr === "CLOSED";
    const disableAttributes = isClosed ? "disabled" : "";

    // Usa los valores que vienen como parámetros si el estado es CLOSED
    const fechaHora = isClosed ? fechahoragrabacion : grabacion;
    const detalleActualizacion = isClosed ? actualizacion : "";

    var modalHtml = `
    <div class="modal fade" id="exampleModalsrcr" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title" id="exampleModalLabel">Administrar Caso #:  ${codigosr}</h5> <!-- RMA -->
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <form>
                        <fieldset>
                            <div class="form-group">
                                <span id="idregistrosrdbcrly" name="idregistrosrdbcrly">Registro dbrma: </span>
                                <span id="idregistrosrdbcr" name="idregistrosrdbcr">${registrosractividadsr}</span>
                            </div>

                            <div class="form-group">
                                <span id="idrmaactualrmacridly" name="idrmaactualrmacridly">Registro dbcierre </span>
                                <span id="idrmaactualrmacrid" name="idrmaactualrmacrid">${idregistro}</span>
                            </div>

                            <div class="form-group">
                                <span id="idfechahoraactsrmocrly" name="idfechahoraactsrmocrly">Fecha  Hora: </span>
                                <span id="idfechahoraactsrmocr" name="idfechahoraactsrmocr">${fechaHora}</span>
                            </div>

                             <div class="form-group">
                                <span id="idrmaactualrmacrly" name="idrmaactualrmacrly">RMA: </span>
                                <span id="idrmaactualrmacr" name="idrmaactualrmacr">${rma}</span>
                            </div>

                             <div class="form-group">
                                <span id="idrmaactualttrmacrly" name="idrmaactualttrmacrly">Dato: </span>
                                <span id="idrmaactualttrmacr" name="idrmaactualttrmacr">${ttrma}</span>
                            </div>

                            <div class="form-group">
                                <span id="idusuariomodificasrmodcrly" name="idusuariomodificasrmodcrly">Usuario: </span>
                                <span id="idusuariomodificasrmodcr" name="idusuariomodificasrmodcr">${username}</span>
                            </div>

                            <div class="form-group">
                            &nbsp;&nbsp;&nbsp;&nbsp;
                                <input type="date" class="form-control" id="idfechaclosermacr" name="idfechaclosermacr" placeholder="Fecha apertura" required ${disableAttributes}>
                                <small id="emailHelp2" class="form-text text-muted">Fecha de cierre RMA</small>
                            </div>

                            <!-- Campo Actualización -->
                            <div class="form-group">
                            &nbsp&nbsp&nbsp&nbsp
                                <textarea class="form-control" id="idinfoactualizacionsrmodcr" name="idinfoactualizacionsrmodcr"
                                    placeholder="Detalle cierre" rows="3" maxlength="200" oninput="this.value = this.value.substring(0, this.maxLength)" required ${disableAttributes}>${detalleActualizacion}</textarea>
                            </div>

                            <div class="form-group">
                            &nbsp&nbsp&nbsp&nbsp
                            <div class="row">
                                <div class="col-md-4">
                                 &nbsp&nbsp&nbsp&nbsp
                                    <input class="form-control" id="idvendorsrmodaccr" type="text" name="idvendorsrmodaccr" readonly="" value="${vendorsr}">
                                </div>

                                <div class="col-md-4">
                                 &nbsp&nbsp&nbsp&nbsp
                                    <input class="form-control" id="idestadosrmodaccr" type="text" name="idestadosrmodaccr" readonly="" value="${estadosr}">
                                </div>

                                <div class="col-md-4">
                                 &nbsp&nbsp&nbsp&nbsp
                                    <input class="form-control" id="idepaissrmodaccr" type="text" name="idepaissrmodaccr" readonly="" value="${paissr}">
                                </div>
                            </div>
                         </div>
                        </fieldset>
                    </form>
                    &nbsp;&nbsp;&nbsp;&nbsp;
                    <div class="modal-footer">
                        <button id="idopcionessrrcr" type="button" class="btn btn-primary" onclick="cierrasrmodal(); return false;" ${disableAttributes}>
                            Cerrar RMA
                        </button>
                    </div>
                </div>
            </div>
        </div>
    </div>
    `;

    $('body').append(modalHtml);
    $('#exampleModalsrcr').modal('show');
    $('#exampleModalsrcr').on('hidden.bs.modal', function () {
        $(this).remove();
        location.reload();
    });
}


    
    function cierrasrmodal() {
        var registrosr = document.getElementById('idregistrosrdbcr').textContent;
        var fechahoragrabacion = toHexString(document.getElementById('idfechahoraactsrmocr').textContent);
        var rmarecibido = document.getElementById('idrmaactualrmacr').textContent;
        var ttrmarecibido = document.getElementById('idrmaactualttrmacr').textContent;
        var fecharmasr = document.getElementById('idfechaclosermacr').value;
        var actualizacioncierre = document.getElementById('idinfoactualizacionsrmodcr').value;
        var usuariosr = document.getElementById('idusuariomodificasrmodcr').textContent;
        var vendorsr = document.getElementById('idvendorsrmodaccr').value;
        var estadosr = document.getElementById('idestadosrmodaccr').value;
        var paissr = document.getElementById('idepaissrmodaccr').value;
        function getValueOrDefault(value, defaultValue) {
            return (value === undefined || value.trim() === "") ? defaultValue : sanitizeString(value);
        }
    
        if (fecharmasr.trim() === "") {
            alert('El campo de fecha cierre es obligatorio.');
            return;
        }
    
        fecharmasrcierre = toHexString(sanitizeString(fecharmasr));
    
        if (actualizacioncierre.trim() === "") {
            alert('El campo de actualización es obligatorio.');
            return;
        }
    
        rmarecibido = getValueOrDefault(rmarecibido, "0");
        ttrmarecibido = getValueOrDefault(ttrmarecibido, "0");
        actualizacioncierre = getValueOrDefault(actualizacioncierre, "sin_act");
    
        var pageNumber = getPageNumberFromURLsr();
        var url = '/agregar_sr/casossr/' + encodeURIComponent(pageNumber) +
                  '/cierrermas/' + encodeURIComponent(registrosr) + '/' +
                  encodeURIComponent(fechahoragrabacion) + '/' +
                  encodeURIComponent(rmarecibido) + '/' +
                  encodeURIComponent(ttrmarecibido) + '/' +
                  encodeURIComponent(fecharmasrcierre) + '/' +
                  encodeURIComponent(actualizacioncierre) + '/' +
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
                    $('#exampleModalsrcr').modal('hide');
                    $('#exampleModalsrcr').on('hidden.bs.modal', function () {
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
    


  function mostrarActualizaciones(registro) {
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


function sanitizeString(str) {
    str = str.replace(/[\/\?&=#%]/g, '_');  // Reemplazar caracteres problemáticos con '_'
    str = str.replace(/\t/g, ' ');  // Reemplazar tabuladores por espacios
    str = str.trim();  // Elimina espacios en blanco al principio y final de la cadena
    return str || 'sin_dato';  // Si la cadena está vacía, devolver 'sin_dato'
}



function confirmarYEnviarsr() {
    var identificador = document.getElementById('ididentificadorsr').value.trim(); 
    if (!identificador) {
        alert("El campo 'ID caso es obligatori' es obligatorio.");
        return; 
    }

    var confirmar = confirm("¿Desea guardar los cambios?");
    if (confirmar) {
        document.getElementById('idformagregarsr').submit(); 
    } else {
        alert('La acción ha sido cancelada.');
    }
}

function confirmarYEnviaract() {
    var identificador = document.getElementById('ididentificadoract').value.trim();
    if (!identificador) {
        alert("El campo 'ID actividad' es obligatorio.");
        return;
    }

    var confirmar = confirm("¿Desea guardar los cambios?");
    if (confirmar) {
        document.getElementById('idformagregaract').submit();
    } else {
        alert('La acción ha sido cancelada.');
    }
}


function confirmarSalida() {
    var confirmar = confirm("¿Desea salir de la aplicación?");
    if (confirmar) {
        window.location.href = "{% url 'logout' %}";
    } else {
        alert('La acción ha sido cancelada.');
    }
}


