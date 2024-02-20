#!/usr/bin/node
/* computes the number of tasks completed by user id. */

const request = require('request');

request(process.argv[2], (err, res, body) => {
  if (err) {
    console.error(err);
  } else {
    body = JSON.parse(body);
    const obj = {};
    for (user of body) {
      if (!user.completed) {
        continue;
      }
      const id = user.userId.toString();
      if (id in obj) {
        obj[id]++;
      } else {
        obj[id] = 1;
      }
    }
    console.log(obj);
  }
});
