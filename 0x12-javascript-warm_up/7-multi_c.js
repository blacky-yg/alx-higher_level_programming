#!/usr/bin/node
// Print "C is fun" x times

const size = Math.floor(Number(process.argv[1]));

if (isNaN(size)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < parseInt(process.argv[1]); i++) {
    console.log('C is fun');
  }
}
