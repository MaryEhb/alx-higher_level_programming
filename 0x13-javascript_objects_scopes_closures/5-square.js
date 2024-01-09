#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (n) {
    super(n, n);
  }
}

module.exports = Square;
