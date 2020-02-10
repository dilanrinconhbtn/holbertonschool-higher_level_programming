#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let j = 0; j < this.height; j++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    this.width = this.width + this.height;
    this.height = this.width - this.height;
    this.width = this.width - this.height;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
};
