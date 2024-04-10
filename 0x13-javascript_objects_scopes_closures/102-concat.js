#!/usr/bin/node
const fs = require('fs');

const firstFile = process.argv[2];
const secondFile = process.argv[3];
const destination = process.argv[4];

fs.readFile(firstFile, 'utf8', function (err, dataFirst) {
  if (err) {
    throw err;
  }

  fs.readFile(secondFile, 'utf8', function (err, dataSecond) {
    if (err) {
      throw err;
    }

    const fullText = dataFirst + dataSecond;

    fs.writeFile(destination, fullText, (err) => {
      if (err) {
        throw err;
      }
    });
  });
});
