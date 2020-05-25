'use strict';

var fs = require("fs");

const file_data = fs.readFileSync('../data/input02.txt');
const file_string = file_data.toString().trim();
const lines = file_string.split('\n');
const dimensions = lines.map(line => line.split('x').map(dim => parseInt(dim)));

function ribbonRequired(dims) {
    dims.sort((x, y) => x-y);
    return dims[0] + dims[1];
}

function paperRequired(dims) {
    dims.sort((x, y) => x-y);
    let answer = dims[0] * dims[1] * 3;
    answer += dims[0] * dims[2] * 2;
    answer += dims[1] * dims[2] * 2;
    return answer;
}

let total_cost = 0;

dimensions.forEach(element => {total_cost += paperRequired(element)});
console.log(total_cost);
