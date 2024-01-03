#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const dict = {};
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const todos = JSON.parse(body);
    for (let i = 0; i < todos.length; i++) {
      const task = todos[i];
      if (task.completed) {
        if (dict[task.userId] === undefined) {
          dict[task.userId] = 1;
        } else {
          dict[task.userId] += 1;
        }
      }
    }
    console.log(dict);
  }
});
