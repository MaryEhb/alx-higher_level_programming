#!/usr/bin/node
/* prints all characters of a Star Wars movie */

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request.get(url, (err, res, body) => {
  if (err) {
    console.error(err);
  } else {
    const characters = JSON.parse(body).characters;
    for (const url of characters) {
      request.get(url, (err, res, body) => {
        if (err) {
          console.error(err);
        } else {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});
