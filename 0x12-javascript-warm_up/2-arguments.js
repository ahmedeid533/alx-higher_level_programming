#!/usr/bin/node

const { argv } = require('node:process');

if (argv.length > 1) {
  console.log('Arguments found');
} else {
  console.log('No argument');
}
