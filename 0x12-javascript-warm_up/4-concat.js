#!/usr/bin/node
// Print two arguments passed to it, in the following format: “ is ”

console.log(typeof process.argv[2] === 'undefined is undefined' ? 'No argument' : process.argv[2] + ' is ' + process.argv[3]);
