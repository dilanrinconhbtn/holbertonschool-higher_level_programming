#!/usr/bin/node

if (!process.argv[2] || !process.argv[3]) {
  console.log(0);
} else {
  const list = process.argv.slice(2);
  const intArgs = list.sort((a, b) => a - b);
  console.log(intArgs[intArgs.length - 2]);
}
