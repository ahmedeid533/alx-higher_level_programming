#!/usr/bin/node
const request = require('request');
const fs = require('fs');
request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    fs.writeFileSync(process.argv[3], body, 'utf8', function (error, content) {
      console.log(error || content);
    });
  }
});
