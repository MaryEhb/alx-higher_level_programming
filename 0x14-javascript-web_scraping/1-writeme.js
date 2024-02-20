#!/usr/bin/node
/* write a string to a file. */

const fs = require('fs');

try {
  fs.writeFileSync(process.argv[2], process.argv[3], 'utf-8');
} catch (e) {
  console.error(e);
}
