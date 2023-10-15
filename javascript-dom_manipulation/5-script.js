// seleccionar elemento con id update_header
let update_header = document.querySelector('#update_header')

// seleccionar elemento header
let header = document.querySelector('header')

// agregar evento para actualizar header
update_header.addEventListener('click', function(){
    header.textContent = "New Header!!!"
})