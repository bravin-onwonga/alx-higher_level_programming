#!/usr/bin/node

const args = process.argv;

const fileName = args[2];
const fs = require('fs');

fs.readFile(fileName, 'utf-8', (err, data) => {
  if (err) {
    console.log(err);
    return;
  }
  console.log(data);
});
