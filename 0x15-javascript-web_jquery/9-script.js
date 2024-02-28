$(document).ready(() => {
    (async () => {
        const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
        const response = await fetch(url);
        const data = await response.json();
        $('DIV#hello').text(data.hello);
    })();
});