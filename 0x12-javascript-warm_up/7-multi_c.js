#!/usr/bin/node
const args = process.argv;
const x = parseInt(args[2], 10);

if (isNaN(x)) {
  console.log("Missing number of occurrences");
  return;
}

if (x <= 0) {
  return;
}

for (let i = 0; i < x; i++) {
  console.log("C is fun");
}