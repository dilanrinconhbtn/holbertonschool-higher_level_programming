#!/usr/bin/node

const list = process.argv.slice(2);
const num = process.argv.length;
if (num <= 3) {
  console.log('0');
} else {
  list.sort();
  console.log(list[list.length - 2]);
}
