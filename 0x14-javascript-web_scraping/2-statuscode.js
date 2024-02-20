#!/usr/bin/node
/* display the status code of a GET request. */

const request = require('request');

request.get(process.argv[2], (err, res, body) => {
  if (err) {
    console.error(err);
  } else {
    console.log('code:', res.statusCode);
  }
});
