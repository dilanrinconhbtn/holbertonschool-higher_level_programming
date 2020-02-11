#!/usr/bin/node
const request = require('request');
const url = 'http://swapi.co/api/films/' + process.argv[2];
request.get(url, function (err, response, body) {
  if (err) {
    console.error(err);
  } else {
    const obj = JSON.parse(body);
    console.log(obj.title);
  }
});
