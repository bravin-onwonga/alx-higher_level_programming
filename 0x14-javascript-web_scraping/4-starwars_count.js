#!/usr/bin/node

const request = require('request');
let count = 0;

const requestURL = process.argv[2];
const findCharacter = 'https://swapi-api.alx-tools.com/api/people/18/';

request(requestURL, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  body = JSON.parse(body);

  for (const results of body.results) {
    for (const character of results.characters) {
      if (character === findCharacter) {
        count += 1;
      }
    }
  }

  console.log(count);
});
