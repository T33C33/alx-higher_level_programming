#!/usr/bin/node
const args = process.argv;
const size = parseInt(args[2], 10);

if (process.argv[2] === undefined || isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    console.log('X'.repeat(size));
  }
}
