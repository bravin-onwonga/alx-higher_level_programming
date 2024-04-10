#!/usr/bin/node
const dict = require('./101-data.js').dict;
const newObj = {};
const idSet = new Set();

for (const key in dict) {
  idSet.add(dict[key]);
}

for (const id of idSet) {
  const value = [];
  for (const k in dict) {
    if (dict[k] === id) {
      value.push(k);
    }
  }
  newObj[id] = value;
}

console.log(newObj);
