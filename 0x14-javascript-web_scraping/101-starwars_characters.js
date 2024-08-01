#!/usr/bin/node
const request = require('request');

const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const content = JSON.parse(body);
    const characters = content.characters;
    // console.log(characters);
    for (const characterUrl of characters) {
      request.get(characterUrl, (error, response, body) => {
        if (error) {
          console.log(error);
        } else {
          const characterData = JSON.parse(body);
          console.log(characterData.name);
        }
      });
    }
  }
});
