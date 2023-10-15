// seleccionar el elemento del encabezado 
let header = document.querySelector('header')

//seleccionar elemento con id read header
let readheader = document.querySelector('#red_header')

// agregar un evento al elemneto readheader
readheader.addEventListener('click', function(){
    header.style.color = '#FF0000'
})