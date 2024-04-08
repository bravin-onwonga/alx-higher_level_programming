#!/usr/bin/node

const myInt = parseInt(process.argv[2]);
if (!(isNaN(myInt))) {
  console.log('My number: ', myInt);
} else {
  console.log('Not a number');
}
