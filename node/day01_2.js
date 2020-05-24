'use strict';

var fs = require("fs");

const file_string = fs.readFileSync('../data/input01.txt').toString();
const string_array = file_string.split("");

let floor = 0;
let i = 0;

while (floor >= 0) {
    if (string_array[i] === '(') {
        floor += 1;
    } else {
        floor -= 1;
    }
    i += 1;
}

console.log(i);
