#!/usr/bin/node

const num = parseInt(process.argv[2]);

if (isNaN(num)) {
  console.log(1);
} else {
  function factorial (num) {
    if (num < 0) {
      return (-1);
    }

    if (num <= 1) {
      return (1);
    }

    return (num * factorial(num - 1));
  }

  console.log(factorial(num));
}
