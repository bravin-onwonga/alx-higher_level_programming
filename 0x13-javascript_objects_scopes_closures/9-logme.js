#!/usr/bin/node
const printer = print();

function * print () {
  let index = 0;
  while (true) {
    yield index;
    index = index + 1;
  }
}

exports.logMe = function (item) {
  if (item) {
    const n = printer.next().value;
    console.log(n + ': ' + item);
  }
};
