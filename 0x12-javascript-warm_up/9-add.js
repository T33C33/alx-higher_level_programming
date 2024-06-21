#!/urs/bin/node
function add (a, b) {
  const first = parseFloat(a);
  const second = parseFloat(b);

  if (isNaN(first) || isNaN(second)) {
    console.log('NaN');
  } else {
    const result = first + second;
    console.log(result);
  }
}
const args = process.argv;
add(args[2], args[3]);
