document.addEventListener('DOMContentLoaded', function(){
    const inputBusqueda= document.getElementById('search-input');
    const sectionsVet = document.querySelectorAll('.vet-locations section');
    
    inputBusqueda.addEventListener('input', function(){
        filtroVetLocalidad();
    });

    function filtroVetLocalidad() {
        const texto = inputBusqueda.value.toLowerCase();
        sectionsVet.forEach(section => {
            const localidad = section.getAttribute('data-localidad').toLowerCase();
            if (localidad.includes(texto)) {
                section.style.display ='';
            } else {
                section.style.display= 'none';
            }
        });
    }
});