var a = [1, 2, 3, 4, 5];
// name func = (args): returnType => {enter the function logic}
var sum = function () {
    var vals = [];
    for (var _i = 0; _i < arguments.length; _i++) {
        vals[_i] = arguments[_i];
    }
    return vals.reduce(function (p, c) {
        return p + c;
    });
};
console.log(a);
console.log(sum(3, 4, 5));
