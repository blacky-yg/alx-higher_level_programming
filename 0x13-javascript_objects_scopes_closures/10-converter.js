#!/usr/bin/node
// Converts a number from base 10 to another base passed as argument

exports.converter = function (base) {
  function convert (number) {
    return number.toString(base);
  }
  return convert;
};
