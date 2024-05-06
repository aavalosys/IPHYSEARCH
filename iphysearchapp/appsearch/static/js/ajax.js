  function cargarDatos() {
    // Realiza una solicitud AJAX al servidor
    fetch("/about/cargar_datos/", {
    method: "GET",
    })
    .then((response) => response.json())
    .then((data) => {
    const tabla = document.getElementById("tabla-datos");
    const tbody = tabla.getElementsByTagName("tbody")[0];
    tbody.innerHTML = ''; // Limpia el cuerpo de la tabla 
    for (const dato of data.datos) {
        const fila = document.createElement("tr");
        const celdaNombre = document.createElement("td");
        const celdaApellido = document.createElement("td");
        celdaNombre.textContent = dato.nombre;
        celdaApellido.textContent = dato.apellido;
        fila.appendChild(celdaNombre);
        fila.appendChild(celdaApellido);
        tbody.appendChild(fila);
    }
})
.catch((error) => {
console.error('Error:', error);
});
}