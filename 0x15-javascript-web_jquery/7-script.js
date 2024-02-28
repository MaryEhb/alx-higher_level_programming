$(document).ready(() => {
    (async () => {
        const url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
        const response = await fetch(url);
        const data = await response.json();
        const name = data.name;
        $('DIV#character').text(name);
    })();
});