#!/usr/bin/node
const lst = require('./100-data.js').list;
const newLst = lst.map((n, index) => n * index);
console.log(lst);
console.log(newLst);
