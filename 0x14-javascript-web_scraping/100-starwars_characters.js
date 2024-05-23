#!/usr/bin/node

const request = require('request');

const filmId = process.argv[2];
const requestURL = 'https://swapi-api.alx-tools.com/api/films';

request(requestURL, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  body = JSON.parse(body);
  const filmData = body.results[filmId - 1];

  for (const characterURL of filmData.characters) {
    request(characterURL, function (error, response, body) {
      if (error) {
        console.log(error);
      }
      body = JSON.parse(body);
      console.log(body.name);
    });
  }
});
