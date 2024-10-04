document.addEventListener('DOMContentLoaded', function(){
    const inputBusqueda= document.getElementById('search-input');
    const botonesVet = document.querySelectorAll('.vet-locations button');
    
    inputBusqueda.addEventListener('input', function(){
        filtroVetLocalidad();
    });

    function filtroVetLocalidad() {
        const texto = inputBusqueda.value.toLowerCase();
        botonesVet.forEach(boton => {
            const localidad = boton.getAttribute('data-localidad').toLowerCase();
            if (localidad.includes(texto)) {
                boton.style.display ='';
            } else {
                boton.style.display= 'none';
            }
        });
    }
});