#!/usr/bin/node
const request = require('request');

const filmId = process.argv[2];
const filmUrl = `https://swapi-api.alx-tools.com/api/films/${filmId}`;

request.get(filmUrl, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const filmData = JSON.parse(body);
    const characters = filmData.characters;
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
