#!/usr/bin/node

const args = process.argv;
const fileName = args[2];
const content = args[3];

const fs = require('fs');

fs.writeFile(fileName, content, 'utf-8', (err) => {
  if (err) {
    console.log(err);
  }
});
