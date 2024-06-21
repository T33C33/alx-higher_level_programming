#!/usr/bin/node
function factorial (x) {
  if (x <= 1) {
    return 1;
  }
  return x * factorial(x - 1);
}
const args = process.argv;
const entry = parseInt(args[2], 10);

if (isNaN(entry)) {
  console.log(1);
} else {
  console.log(factorial(entry));
}
