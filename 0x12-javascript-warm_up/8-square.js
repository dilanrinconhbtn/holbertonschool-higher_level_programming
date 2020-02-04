#!/usr/bin/node
const argu = process.argv[2];
const myword = 'X';
if (process.argv.length > 2) {
  for (let j = 0; j < argu; j++) {
    console.log(myword.repeat(argu));
  }
} else {
  console.log('Missing size');
}
