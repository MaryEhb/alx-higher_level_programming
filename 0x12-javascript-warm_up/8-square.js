#!/usr/bin/node

let line;
if (isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  for (let i = 0; i < process.argv[2]; i++) {
    line = '';
    for (let j = 0; j < process.argv[2]; j++) {
      line += 'X';
    }
    console.log(line);
  }
}
