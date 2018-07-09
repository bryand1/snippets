/*
 * Filter list items by type using arrow function
 */

var a = ['x', 1, 'y', 2, 'z', 3]
var b = a.filter(x => typeof x === 'number')
console.log(b)  // [ 1, 2, 3 ]
