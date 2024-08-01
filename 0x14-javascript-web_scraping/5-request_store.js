#!/usr/bin/node
// lorem ipsum
const request = require('request');
const fs = require('fs');

request.get(process.argv[2], (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    fs.writeFile(process.argv[3], body, 'utf-8', (err) => {
      if (err) {
        console.log(err);
      }
    });
  }
});
