// seleccionar el elemento del encabezado
let header = document.querySelector('header');

// selccionar el elemento del encabezado 
let readheader = document.querySelector('#red_header');

// agregar un evento click al elemento red header
readheader.addEventListener('click', function(){
    header.classList.add('red')
})