#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let count = 0;

  list.forEach(ele => {
    if (ele === searchElement) {
      count++;
    }
  });
  return count;
};
