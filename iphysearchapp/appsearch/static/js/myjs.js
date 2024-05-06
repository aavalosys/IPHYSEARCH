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

function onloadpagewelcome() { 
    var selectBox = document.getElementById("selectdbwel");
    var elementoplace =selectBox.options[0].value;
    document.getElementById("iddbselectedwel").value = elementoplace; 
    return;
}

function copiaripnodo(ipnodo) { 
    document.getElementById("idtxtip").value = ipnodo;
    return;
}

function copiaselectdbs(){
    var selectedValue = document.getElementById('selectdbwel').value;
    document.getElementById('iddbselectedwel').value = selectedValue;
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

