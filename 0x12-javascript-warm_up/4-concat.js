#!/usr/bin/node

if (process.argv[1] === undefined) {
  console.log('undefined is undefined');
} else if (process.argv[2] === undefined) {
  console.log(`${process.argv[1]} is undefined`);
} else {
  console.log(`${process.argv[1]} is ${process.argv[2]}`);
}
