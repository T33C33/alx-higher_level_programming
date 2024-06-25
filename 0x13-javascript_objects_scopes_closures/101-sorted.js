#!/usr/bin/node
const dict = require('./101-data').dict;
const occurById = {};
for (const key in dict) {
  const occurrences = dict[key];

  if (!occurById[occurrences]) {
    occurById[occurrences] = [];
  }

  occurById[occurrences].push(key);
}

console.log(occurById);
