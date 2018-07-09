/*
 * Function.prototype.bind()
 *
 * The bind() method creates a new function that, when called, has its `this` keyword set
 * to the provided value, with a given sequence of arguments preceding any provided when
 * the new function is called.
 *
 * function.bind(thisArg[, arg1[, arg2[, ...]]])
 * 
 * Parameters
 *
 * thisArg
 *   The value to be passed as the `this` parameter to the target function when the bound
 *   function is called. The value is ignored if the bound function is constructed using the
 *   `new` operator.
 *
 * arg1, arg2, ...
 *    Arguments to prepend to arguments provided to the bound function when invoking
 *    the target function.
 *
 * Return value
 *   A copy of the given function with the specified `this` value and initial arguments.
 */

var module = {
    x: 42,
    getX: function() {
        return this.x;
    }
}

var unboundGetX = module.getX;
console.log(unboundGetX());  // undefined

var boundGetX = unboundGetX.bind(module);
console.log(boundGetX());  // 42
