#!/usr/bin/node

const request = require('request');
const id = process.argv[2];

const requestURL = `https://swapi-api.alx-tools.com/api/films/${id}`;

request(requestURL, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  body = JSON.parse(body);
  console.log(body.title);
});
