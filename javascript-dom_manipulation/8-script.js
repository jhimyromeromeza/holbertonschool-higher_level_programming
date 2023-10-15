document.addEventListener('DOMContentLoaded', function(){
    fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
    .then(response => response.json())
    .then(data => {
        let hello = document.querySelector('#hello')
        hello.textContent = data.hello
    })
    .catch(error => console.error('Error: ', error))
})