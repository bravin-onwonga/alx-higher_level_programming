#!/usr/bin/node

const request = require('request');
let count = 0;

const requestURL = process.argv[2];

request(requestURL, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  body = JSON.parse(body);

  for (const results of body.results) {
    for (const characterURL of results.characters) {
      let id = characterURL[characterURL.length - 2];

      if (characterURL[characterURL.length - 3] !== '/') {
        id = `${characterURL[characterURL.length - 3]}${id}`;
      }
      if (id === '18') {
        count += 1;
      }
    }
  }
  console.log(count);
});
