#!/usr/bin/node
function add (a, b) {
  const first = parseFloat(a);
  const second = parseFloat(b);
  const result = first + second;

  if ((first === undefined || isNaN(first)) && (second === undefined || isNaN(second))) {
    console.log('NaN');
  } else {
    console.log(result);
  }
}

add(Number(process.argv[2]), Number(process.argv[3]));
