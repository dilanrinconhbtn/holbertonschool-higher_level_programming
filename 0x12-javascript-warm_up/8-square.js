#!/usr/bin/node
const argu = parseInt(process.argv[2]);
const myword = 'X';
if (!argu) {
  console.log('Missing size');
} else {
  for (let j = 0; j < argu; j++) {
    console.log(myword.repeat(argu));
  }
}
