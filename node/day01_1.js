'use strict';

var fs = require("fs");

const file_data = fs.readFileSync('../data/input01.txt');
const file_string = file_data.toString();

const num_opens = (file_string.match(/\(/g)).length;
const num_closes = (file_string.match(/\)/g)).length;

console.log(num_opens - num_closes);
