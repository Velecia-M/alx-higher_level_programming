#!/usr/bin/node
/* script that prints a square */
const size = process.argv[2];

if (size === undefined || isNaN(parseInt(size))) {
  console.log('Missing size');
} else {
  for (let i = 0; i < parseInt(size); i++) {
    let line = '';
    for (let j = 0; j < parseInt(size); j++) {
      line = 'X';
    }
    console.log(line);
  }
}
