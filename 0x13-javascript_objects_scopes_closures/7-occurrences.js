#!/usr/bin/node
// Prints the number of occurrences in a list

exports.nbOccurences = function (list, searchElement) {
  let num = 0;
  list.forEach(element => {
    if (element === searchElement) num++;
  });
  return num;
};
