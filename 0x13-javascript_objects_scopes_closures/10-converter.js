#!/usr/bin/node
exports.converter = function (base) {
  if (base === 10) {
    return baseDec;
  }

  if (base === 16) {
    return baseHex;
  }

  if (base === 2) {
    return baseBin;
  }

  if (base === 8) {
    return baseOctal;
  }
};

function baseDec (num) {
  return (num);
}

function baseHex (num) {
  return (num.toString(16));
}

function baseOctal (num) {
  return (num.toString(8));
}
function baseBin (num) {
  return (num.toString(2));
}
