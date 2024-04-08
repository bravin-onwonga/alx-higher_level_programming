#!/usr/bin/node

const myInt = parseInt(process.argv[2]);

if (!(isNaN(myInt))) {
  for (let i = 0; i < myInt; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
