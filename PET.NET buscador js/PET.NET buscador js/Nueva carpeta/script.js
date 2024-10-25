document.addEventListener('DOMContentLoaded', function(){
    const inputBusqueda = document.getElementById('search-input');
    const contenedores = document.querySelectorAll('.main-container');
    
    inputBusqueda.addEventListener('input', function(){
        filtrarPorLocalidad();
    });

    function filtrarPorLocalidad() {
        const texto = inputBusqueda.value.toLowerCase();
        contenedores.forEach(contenedor => {
            const localidad = contenedor.getAttribute('data-localidad').toLowerCase();
            if (localidad.includes(texto)) {
                contenedor.style.display = ''; // Mostrar si coincide
            } else {
                contenedor.style.display = 'none'; // Ocultar si no coincide
            }
        });
    }
});

