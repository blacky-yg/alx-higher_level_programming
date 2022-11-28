#!/usr/bin/node

const sentence = 'C is fun';

if (process.argv[1] === undefined) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < parseInt(process.argv[1]); i++) {
    console.log(sentence);
  }
}
