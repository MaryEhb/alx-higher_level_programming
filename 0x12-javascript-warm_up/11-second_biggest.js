#!/usr/bin/node

if (process.argv.length <= 3) {
  console.log(0);
} else {
  let m = Math.max(parseInt(process.argv[2]), parseInt(process.argv[3]));
  let n = Math.min(parseInt(process.argv[2]), parseInt(process.argv[3]));

  for (let i = 4; i < process.argv.length; i++) {
    if (parseInt(process.argv[i]) > m) {
      n = m;
      m = parseInt(process.argv[i]);
    }
  }
  console.log(n);
}
