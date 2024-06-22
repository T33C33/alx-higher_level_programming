#!/usr/bin/node

const args = process.argv.slice(2);

if (args.length < 2) {
  console.log(0);
} else {
  const conv = args.map(Number);
  const uniqNum = Array.from(new Set(conv));

  uniqNum.sort((a, b) => b - a);

  if (uniqNum.length < 2) {
    console.log(0);
  } else {
    console.log(uniqNum[1]);
  }
}
