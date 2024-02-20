#!/usr/bin/node
/* prints all characters of a Star Wars movie */

const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

// Function to fetch and print character names sequentially
function fetchAndPrintCharacter (urlArray, index) {
  if (index >= urlArray.length) {
    return; // Exit when all characters have been printed
  }

  const characterUrl = urlArray[index];
  request.get(characterUrl, (err, res, body) => {
    if (err) {
      console.error(err);
    } else {
      console.log(JSON.parse(body).name);
      fetchAndPrintCharacter(urlArray, index + 1); // Fetch next character recursively
    }
  });
}

request.get(url, (err, res, body) => {
  if (err) {
    console.error(err);
  } else {
    const characters = JSON.parse(body).characters;
    fetchAndPrintCharacter(characters, 0); // Start fetching characters sequentially
  }
});
