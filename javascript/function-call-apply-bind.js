// https://stackoverflow.com/questions/15455009/javascript-call-apply-vs-bind
const obj1 = {"firstName": "Bob", "lastName": "Smith"};
const obj2 = {"firstName": "Alice", "lastName": "Trent"};

function greeting(msg) {
  return `${this.firstName} ${this.lastName}: ${msg}`; 
}

// Function.prototype.call()
console.log(greeting.call(obj1, 'Hello'));

// Function.prototype.apply()
console.log(greeting.apply(obj2, ['Hello']));

// Function.prototype.bind()
const boundGreeting = greeting.bind(obj1);
console.log(boundGreeting('Hello'));
