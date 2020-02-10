#!/usr/bin/node
const Rectangle = require('./5-square');
module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (!c) {
      for (let j = 0; j < this.height; j++) {
        console.log('X'.repeat(this.width));
      }
    } else {
      for (let j = 0; j < this.height; j++) {
        console.log('C'.repeat(this.width));
      }
    }
  }
};
