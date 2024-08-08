#!/usr/bin/node
const request = require('request');

const movieID = process.argv[2];

function getMovie (movieID, callback) {
  const url = `https://swapi-api.alx-tools.com/api/films/${movieID}`;
  request(url, (error, response, body) => {
    if (error) {
      console.error('Failed to fetch data:', error);
      return callback(error, null);
    }
    if (response.statusCode === 200) {
      try {
        const data = JSON.parse(body);
        callback(null, data);
      } catch (err) {
        console.error('Failed to parse JSON:', err);
        callback(err, null);
      }
    } else {
      console.error('Request failed with status code:', response.statusCode);
      callback(new Error(`Request failed with status code ${response.statusCode}`), null);
    }
  });
}

function printCharacters (movieID) {
  getMovie(movieID, (error, data) => {
    if (error) {
      console.error('Error:', error);
      return;
    }
    const characters = data.characters;

    if (!characters || characters.length === 0) {
      console.log('No characters found.');
      return;
    }

    characters.forEach(characterUrl => {
      request(characterUrl, (error, response, body) => {
        if (error) {
          console.error('Failed to fetch character:', error);
          return;
        }
        if (response.statusCode === 200) {
          try {
            const charData = JSON.parse(body);
            console.log(charData.name);
          } catch (err) {
            console.error('Failed to parse character JSON:', err);
          }
        } else {
          console.error('Failed to fetch character:', response.statusCode);
        }
      });
    });
  });
}

printCharacters(movieID);
