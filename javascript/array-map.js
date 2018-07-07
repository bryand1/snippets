/*
 * Apply transformation to each array item using map and arrow function
 */

var a = ['a', 'b', 'c']
var b = a.map(x => x.toUpperCase())
console.log(b)  // [ 'A', 'B', 'C' ]
