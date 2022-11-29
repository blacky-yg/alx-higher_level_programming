#!/usr/bin/node
// Concatenate two / three files

const fs = require('fs');

function callback (err, data) {
  if (err) {
    return console.log(err);
  }
  fs.appendFile(process.argv[4], data, function (err) {
    if (err) console.log(err);
  });
}

fs.readFile(process.argv[2], 'utf8', callback);
fs.readFile(process.argv[3], 'utf8', callback);
