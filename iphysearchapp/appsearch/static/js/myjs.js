
function onloadpag() {
    var selectBox = document.getElementById("selectdb");
    var elementoplace =selectBox.options[0].value;
    document.getElementById("idtxtdb").value = elementoplace; 
    document.getElementById("idtxtdbrbs").value = elementoplace;
    return;
}

function copiaseleccionado() {
    var selectBox = document.getElementById("selectdb");
    var valorseleccionado = selectBox.options[selectBox.selectedIndex].value;
    document.getElementById("idtxtdb").value = valorseleccionado;
    document.getElementById("idtxtdbrbs").value = valorseleccionado; 
    return;
}

function copiaripnodo(ipnodo) {    //copia el valor seleccionado con clic en el input IDRBS
    document.getElementById("idtxtip").value = ipnodo;
    return;
}
