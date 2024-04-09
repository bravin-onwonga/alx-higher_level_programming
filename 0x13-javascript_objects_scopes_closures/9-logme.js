#!/usr/bin/node
exports.logMe = function (item) {
  let i = 0;

  while (item) {
    yield i;
    console.log(i + ' : ' + item);
  }
};
