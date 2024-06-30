#!/usr/bin/node

if (!process.argv[2] || !process.argv[3]) {
  console.log(0);
} else {
  let biggest = parseInt(process.argv[2]);
  let secBig = parseInt(process.argv[3]);
  for (let i = 2; i < process.argv.length; i++) {
    if (parseInt(process.argv[i]) > biggest) {
      biggest = parseInt(process.argv[i]);
    }
  }
  for (let j = 2; j < process.argv.length; j++) {
    if (parseInt(process.argv[j]) < biggest && parseInt(process.argv[j]) > secBig) {
      secBig = parseInt(process.argv[j]);
    }
  }
  console.log(secBig);
}
