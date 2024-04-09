#!/usr/bin/node

exports.callMeMoby = function (number, theFunction) {
  while (number > 0) {
    theFunction();
    number--;
  }
};
