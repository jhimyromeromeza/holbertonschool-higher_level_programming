// seleccionar elemento de la etiqueta div
let add_item = document.querySelector('#add_item')
// seleccionar elemento de la etiqueta ul
let class_mylist = document.querySelector('.my_list')

// agregar evento de click a ul
add_item.addEventListener('click', function(){
    new_item = document.createElement('li');
    new_item.textContent = 'item'
    class_mylist.appendChild(new_item)

})