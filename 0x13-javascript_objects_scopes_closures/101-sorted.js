#!/usr/bin/node

const data = require('./101-data').dict;

const obj = {};

for (const i in data) {
  if (data[i] in obj) {
    obj[data[i]].push(i);
  } else {
    obj[data[i]] = [i];
  }
}

console.log(obj);
