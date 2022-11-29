#!/usr/bin/node
// List of integers displayed with a function map

const list = require('./100-data').list;
const mapped = list.map(function (value, index) { return value * index; });

console.log(list);
console.log(mapped);
