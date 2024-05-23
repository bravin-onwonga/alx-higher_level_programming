#!/usr/bin/node

const request = require('request');

const filmId = process.argv[2];
const requestURL = 'https://swapi-api.alx-tools.com/api/films';

const myLst = [];

request(requestURL, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  body = JSON.parse(body);
  const filmData = body.results[filmId - 1];

  for (const characterURL of filmData.characters) {
    let id = characterURL[characterURL.length - 2];
    if (characterURL[characterURL.length - 3] !== '/') {
      id = `${characterURL[characterURL.length - 3]}${id}`;
    }
    myLst.push(id);
  }
  for (const charId of myLst) {
    const nameURL = `https://swapi-api.alx-tools.com/api/people/${charId}/`;

    request(nameURL, function (error, response, body) {
      if (error) {
        console.log(error);
      }
      body = JSON.parse(body);
      console.log(body.name);
    });
  }
});
