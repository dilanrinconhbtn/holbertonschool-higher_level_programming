#!/usr/bin/node
const f = parseInt(process.argv[2]);
let total = 0;
function facotrial (a) {
  if (!a) {
    return (1);
  } else {
    return (a * facotrial(a - 1));
  }
}
total = facotrial(f);
console.log(total);
