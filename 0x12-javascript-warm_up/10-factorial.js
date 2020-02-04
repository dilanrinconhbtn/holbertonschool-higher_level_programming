#!/usr/bin/node

function facotrial (a) {
  var total = 1;
  for (let i = 1; i <= a; i++) {
    total = total * i;
  }
  console.log(total);
}

const argu = parseInt(process.argv[2], 10);
facotrial(argu);
