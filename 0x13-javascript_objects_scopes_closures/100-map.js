#!/usr/bin/node

const list = require('./100-data').list;

console.log(list);
let count = -1;
const list1 = list.map((i) => {
  count++;
  return count * i;
});
console.log(list1);
