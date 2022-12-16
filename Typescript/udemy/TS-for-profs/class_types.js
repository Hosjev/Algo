var Queue = /** @class */ (function () {
    function Queue() {
        // public by default
        this.data = [];
    }
    // method name (args): RT
    Queue.prototype.push = function (item) {
        this.data.push(item);
    };
    Queue.prototype.pop = function () {
        return this.data.shift();
    };
    return Queue;
}());
// num type and instantiate class object
var numsQ = new Queue();
numsQ.push(1);
numsQ.push(2);
numsQ.push(3);
numsQ.push(4);
numsQ.push(5);
console.log(numsQ.pop());
console.log(numsQ.pop().toPrecision());
// num type and instantiate class object
var stringsQ = new Queue();
stringsQ.push('foo');
stringsQ.push('bar');
stringsQ.push('bear');
stringsQ.push('zoo');
stringsQ.push('dump');
console.log(stringsQ.pop());
