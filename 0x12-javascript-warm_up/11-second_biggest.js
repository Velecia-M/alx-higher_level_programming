#!/usr/bin/node
/* A script that searches the second biggest integer in the list of arguments.
 */
const args = process.argv;

if (args.length <= 3) {
  console.log('0');
} else {
  let int2 = parseInt(args[2]);
  let highest = parseInt(args[3]);
  for (let i = 2; i < args.length; i++) {
    const num = parseInt(args[i]);
    if (num > highest) {
      int2 = highest;
      highest = num;
    } else if (num > int2 && num < highest) {
      int2 = num;
    }
  }
  console.log(int2);
}
