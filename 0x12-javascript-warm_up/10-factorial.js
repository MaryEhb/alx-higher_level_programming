#!/usr/bin/node

function fact (a) {
  if (a > 1) {
    return a * fact(a - 1);
  }
  return 1;
}

if (!isNaN(process.argv[2])) {
  console.log(fact(parseInt(process.argv[2])));
} else {
  console.log(1);
}
