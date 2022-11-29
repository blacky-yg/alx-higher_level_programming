#!/usr/bin/node
// Class Square that defines a square and inherits from Rectangle of 4-rectangle.js (char print)
const SquareModel = require('./5-square');

module.exports = class Square extends SquareModel {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    this.print(c);
  }
};
