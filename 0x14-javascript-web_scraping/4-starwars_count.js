#!/usr/bin/node
/* prints the number of Star Wars films a character appears in. */

const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films/';
const characterURL = 'https://swapi-api.alx-tools.com/api/people/18/';
request.get(url, (err, res, body) => {
  if (err) {
    console.error(err);
  } else {
    let count = 0;
    const result = JSON.parse(body).results;
    for (const film of result) {
      if (film.characters.includes(characterURL)) {
        count++;
      }
    }
    console.log(count);
  }
});
