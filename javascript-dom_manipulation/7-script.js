fetch('https://swapi-api.hbtn.io/api/films/?format=json')
.then(response => response.json())
.then(data => {
    let list = document.querySelector('#list_movies');
    for(let movie of data.results){
        let li = document.createElement('li');
        li.textContent = movie.title;
        list.append(li);
    }})
.catch(error => console.error('Error: ', error))

