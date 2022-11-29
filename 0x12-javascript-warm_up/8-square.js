#!/usr/bin/node

const size = Math.floor(Number(process.argv[1]));

if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    console.log('X'.repeat(size));
  }
}
