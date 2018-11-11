let arr = [4, 14, 25, 26, 31, 3333, 8, 2];

// Find index of first array element divisible by 3
const f = (elem) => (elem % 3) === 0;

console.log(arr.findIndex(f));  // 5

