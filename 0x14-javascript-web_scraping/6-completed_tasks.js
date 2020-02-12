#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
var dic = {};
var counter = 1;
request(url, function (err, response, body) {
  if (err) {
    console.error(err);
  } else {
    const obj = JSON.parse(body);
    for (const x in obj) {
      if (obj[x].completed === true) {
        if (obj[x].userId in dic) {
          counter++;
          dic[obj[x].userId] = counter;
        } else {
          counter = 1;
          dic[obj[x].userId] = counter;
        }
      }
    }
    console.log(dic);
  }
});
