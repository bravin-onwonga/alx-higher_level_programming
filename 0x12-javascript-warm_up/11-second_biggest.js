#!/usr/bin/node
let i = 2;
let k = 0;
const myArr = [];

while (process.argv[i]) {
  myArr[k] = parseInt(process.argv[i]);
  i++;
  k++;
}

function compareNumbers (a, b) {
  return a - b;
}

if (myArr.length < 2) {
  console.log(0);
} else {
  console.log(myArr.sort(compareNumbers).reverse()[1]);
}
