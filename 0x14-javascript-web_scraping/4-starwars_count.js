#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
let count = 0;
request(url, function (err, response, body) {
  if (err) {
    console.error(err);
  } else {
    const obj = JSON.parse(body).results;
    for (const film of obj) {
      for (const charac of film.characters) {
        if (charac.search('/18/') > 0) {
          count++;
        }
      }
    }
  }
  console.log(count);
});
