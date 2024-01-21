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






