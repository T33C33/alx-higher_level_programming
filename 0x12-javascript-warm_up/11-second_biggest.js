#!/usr/bin/node
const args = process.argv.slice(2);
if ((args === undefined) || (process.argv.slice(2).length === 1)) {
  console.log(0);
} else {
  const conv = args.map(Number);
  const uniqNum = Array.from(new Set(conv));
  uniqNum.sort((a, b) => b - a);
  console.log(uniqNum[1]);
}
