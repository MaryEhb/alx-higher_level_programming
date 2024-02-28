$(document).ready(() => {
    (async () => {
        const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
        const response = await fetch(url);
        const data = await response.json();
        const results = data.results;
        for (let i = 0; i < results.length; i++) {
            $('UL#list_movies').append(`<li>${results[i].title}</li>`);
        }
    })();
});