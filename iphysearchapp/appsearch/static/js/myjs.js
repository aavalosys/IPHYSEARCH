function onloadpag() {
    var selectBox = document.getElementById("selectdb");
    var elementoplace =selectBox.options[0].value;
    document.getElementById("idtxtdb").value = elementoplace; 
    document.getElementById("idtxtdbrbs").value = elementoplace;
    return;
}

function onloadpagevarios() { 
    var selectBox = document.getElementById("selectdb");
    var elementoplace =selectBox.options[0].value;
    document.getElementById("idtxtdb").value = elementoplace; 
    return;
}

function copiaseleccionado() {
    var selectBox = document.getElementById("selectdb");
    var valorseleccionado = selectBox.options[selectBox.selectedIndex].value;
    document.getElementById("idtxtdb").value = valorseleccionado;
    document.getElementById("idtxtdbrbs").value = valorseleccionado; 
    return;
}

function copiaripnodo(ipnodo) { 
    document.getElementById("idtxtip").value = ipnodo;
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







