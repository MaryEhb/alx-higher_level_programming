#!/usr/bin/node
/* prints the number of Star Wars films a character appears in. */

const request = require('request');

const searchPage = (n, callback) => {
  const url = 'https://swapi-api.alx-tools.com/api/people/?page=' + n;
  request.get(url, (err, res, body) => {
    if (err) {
      console.error(err);
      callback(err, null);
    } else {
      const result = JSON.parse(body).results;
      for (const key in result) {
        if (result[key].name === 'Wedge Antilles') {
          const characterURL = result[key].url;
          callback(null, characterURL);
          return;
        }
      }
      searchPage(n + 1, callback);
    }
  });
};

searchPage(1, (err, characterURL) => {
  if (err) {
    console.error(err);
  } else {
    const url = 'https://swapi-api.alx-tools.com/api/films/';
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
  }
});
