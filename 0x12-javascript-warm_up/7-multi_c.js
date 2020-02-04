#!/usr/bin/node
const argu = process.argv[2];
if (argu === undefined) {
  console.log('Missing number of occurrences');
} else {
  for (let index = 0; index < argu; index++) {
    console.log('C is fun');
  }
}
