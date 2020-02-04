#!/usr/bin/node

function add (a, b) {
  const x = a + b;
  console.log(x);
}

const first = parseInt(process.argv[2], 10);
const second = parseInt(process.argv[3], 10);
add(first, second);
