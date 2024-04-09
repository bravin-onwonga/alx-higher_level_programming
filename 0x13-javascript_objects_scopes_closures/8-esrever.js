#!/usr/bin/node
exports.esrever = function (list) {
  const newList = [];
  let j = list.length - 1;
  let i = 0;

  while (j >= 0) {
    newList[i] = list[j];
    j--;
    i++;
  }
  return (newList);
};
