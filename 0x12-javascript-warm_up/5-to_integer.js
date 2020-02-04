#!/usr/bin/node
const argu = process.argv[2];
const integer = parseInt(argu, 10);
if (isNaN(integer)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + integer);
}
