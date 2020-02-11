#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const character = 'https://swapi.co/api/people/18/';
let count = 0;
request(url, function (err, response, body) {
  if (err) {
    console.error(err);
  } else {
    const obj = JSON.parse(body);
    for (const x in obj.results) {
      for (const y in obj.results[x].characters) {
        if (obj.results[x].characters[y] === character) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
