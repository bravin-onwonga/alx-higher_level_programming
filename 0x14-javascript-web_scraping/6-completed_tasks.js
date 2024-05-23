#!/usr/bin/node

const request = require('request');
const requestURL = process.argv[2];

request(requestURL, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const myObj = {};
  body = JSON.parse(body);

  for (const item of body) {
    const id = item.userId.toString();
    if (item.completed === true) {
      if (id in myObj) {
        myObj[id] += 1;
      } else {
        myObj[id] = 1;
      }
    }
  }
  console.log(myObj);
});
