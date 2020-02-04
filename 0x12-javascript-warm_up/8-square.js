#!/usr/bin/node
const argu = process.argv[2];
const myword = 'X'
for (let j = 0; j < argu; j++) {
    console.log(myword.repeat(argu));
}
