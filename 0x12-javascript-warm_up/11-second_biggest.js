#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log('0');
} else {
  const numbers = process.argv.slice(2).map(Number);
  const sorted = numbers.sort(function (a, b) { return b - a; });
  console.log(sorted[1]);
}
