#!/usr/bin/node
const args = process.argv;
const x = parseInt(args[2], 10);

if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else if (x > 0) {
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
}
