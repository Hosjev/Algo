"use strict";
/*
* Type checking IS done on arguments
* (the non-explicit passing of 'argument name'
*  that happens to match what's in the object evals to true)
* The above statement is TRUE in the Chipper stack, not here
* *the point here is that type checking IS done
*/
exports.__esModule = true;
var Currency;
(function (Currency) {
    Currency["USD"] = "USDollar";
})(Currency || (Currency = {}));
function money(opts) {
    /* do stuff, return thing */
    return opts.amount + " " + opts.currency;
}
exports.money = money;
var myCurr = Currency.USD;
var myAmt = 3;
var result = money({
    currency: myCurr,
    amount: myAmt
});
console.log("print this hotmess: " + result);
