function makeIterator(array) {
  let index = 0
  return {
    next: function() {
      return index < arr.length ?
        {value: arr[index++], done: false} :
        {done: true};
      }
  };
}

arr = [1, 2, 3]
it = makeIterator(arr)
console.log(it.next().value)  // 1
console.log(it.next().value)  // 2
console.log(it.next().value)  // 3
console.log(it.next().done)   // true
