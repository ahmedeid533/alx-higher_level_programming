#!/usr/bin/node

const num = parseInt(process.argv[2]);

if (isNaN(num)) {
  console.log('Not a number');
} else {
  for (let i = 0; i < num; i++) {
    console.log('C is fun');
  }
}
