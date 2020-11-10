// const arr = ["a", "b", "c", "d", "e"];

// // target, start, end
// const methodReturn = arr.copyWithin(3);

// console.log(arr); // ["c", "b", "a"]
// console.log(methodReturn); // ["c", "b", "a"]

const arr = [];

arr.length = 5;
console.log(arr.fill(0));
console.log(arr);
