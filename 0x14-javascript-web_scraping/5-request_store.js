#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const requestURL = process.argv[2];
const fileName = process.argv[3];

request(requestURL, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  fs.writeFile(fileName, body, 'utf-8', (err) => {
    if (err) {
      console.log(err);
    }
  });
});
