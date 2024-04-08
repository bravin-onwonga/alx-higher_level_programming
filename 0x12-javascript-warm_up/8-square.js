#!/usr/bin/node

const myInt = parseInt(process.argv[2]);

if (!(isNaN(myInt))) {
  for (let i = 0; i < myInt; i++) {
    let myStr = '';
    for (let n = 0; n < myInt; n++) {
      myStr = myStr + 'X';
    }
    console.log(myStr);
  }
} else {
  console.log('Missing size');
}
