#!/usr/bin/node
const oldSquare = require('./5-square');

class Square extends oldSquare {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let matrix = '';
      for (let j = 0; j < this.width; j++) {
        matrix += c;
      }
      console.log(matrix);
    }
  }
}
module.exports = Square;
