#!/usr/bin/node

if (process.argv[1] === undefined || process.argv[2] === undefined) {
  console.log('NaN');
} else {
  console.log(parseInt(process.argv[2]) + parseInt(process.argv[3]));
}
