#!/usr/bin/node

const request = require('request');

const requestURL = process.argv[2];

request(requestURL, function (error, response) {
  if (error) {
    console.log(error);
  }
  console.log(`code: ${response.statusCode}`);
});
