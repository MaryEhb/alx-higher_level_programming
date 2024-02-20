#!/usr/bin/node
/* reads and prints the content of a file. */

const fs = require('fs');

try {
  const read = fs.readFileSync(process.argv[2], 'utf-8');
  console.log(read);
} catch (e) {
  console.error(e);
}
