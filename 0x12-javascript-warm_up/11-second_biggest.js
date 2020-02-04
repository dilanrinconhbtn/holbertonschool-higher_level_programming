#!/usr/bin/node

const argu = process.argv.length;
let max = '';
let min = '';
let number = '';
for (let i = 2; i < argu; i++) {
  if (process.argv[i] > max) {
    max = process.argv[i];
    number = i;
  }
  if (number !== i && process.argv[i] > min) {
    min = process.argv[i];
  }
}
if (min === '') {
  console.log('0');
} else {
  console.log(min);
}
