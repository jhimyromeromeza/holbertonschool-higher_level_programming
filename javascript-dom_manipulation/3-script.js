// seleccionar elemento del encabezado
let header = document.querySelector('header');

// seleccionar elemnto de encabezado id toggle_header
let toggle_header = document.querySelector('#toggle_header');

// agregar un evento de click a toogle_header
toggle_header.addEventListener('click', function (){
    // Comprueba si el encabezado tiene la clase 'green'
    if(header.classList.contains('green')){
        // Comprueba si el encabezado tiene la clase 'green'
        header.classList.remove('green')
        header.classList.add('red')
    }else{
        // Comprueba si el encabezado tiene la clase 'green'
        header.classList.remove('red')
        header.classList.add('green')
    }
})