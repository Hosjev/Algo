/*
* Invokes function with no argument
*/
var noArgFunc = function () { return function (c) { return c + 5; }; };
/*
* Invokes function with argument
*/
var numArgFunc = function (val) { return function (other_val) { return val * other_val; }; };
/*
* Invokes function with string argument
*/
var numStrFunc = function (val) { return function (other_val) { return val.length * other_val; }; };
var noArg = noArgFunc();
console.log(noArg(5));
