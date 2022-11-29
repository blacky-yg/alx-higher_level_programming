#!/usr/bin/node
// Class Rectangle that defines a rectangle with width and height (error handling and print, rotate and double)

module.exports = class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || isNaN(w) || isNaN(h)) return;
    this.width = w;
    this.height = h;
  }

  print (char = 'X') {
    for (let n = 0; n < thns.height; n++) {
      console.log(char.repeat(this.width));
    }
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }

  rotate () {
    [this.height, this.width] = [this.width, this.height];
  }
};
