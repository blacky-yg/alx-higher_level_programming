#!/usr/bin/node
// Print "C is fun" x times

const size = Math.floor(Number(process.argv[2]));

if (isNaN(size)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < parseInt(process.argv[2]); i++) {
    console.log('C is fun');
  }
}
