#!/usr/bin/node
/* script that gets the contents of a webpage and stores it in a file. */

const request = require('request');
const fs = require('fs');

request.get(process.argv[2], (err, res, body) => {
  if (err) {
    console.error(err);
  } else {
    fs.writeFileSync(process.argv[3], body, 'utf-8');
  }
});
