var Rect = /** @class */ (function () {
    function Rect(width, height) {
        this.width = width;
        this.height = height;
    }
    Rect.prototype.compareTo = function (value) {
        return (this.width * this.height) - (value.width * value.height);
    };
    return Rect;
}());
var Triangle = /** @class */ (function () {
    function Triangle(width, height) {
        this.width = width;
        this.height = height;
    }
    Triangle.prototype.compareTo = function (value) {
        return this.width * this.height - value.width * value.height;
    };
    return Triangle;
}());
var rec2 = new Rect(3, 5);
var rec1 = new Rect(2, 4);
var diff = rec1.compareTo(rec2);
/* LOGIC */
diff > 0 ? console.log("Rect1 is bigger in area than 2 by: " + diff) :
    diff == 0 ? console.log('Rect1 is same as 2') :
        console.log("Rect1 is smaller in area than 2 by: " + Math.abs(diff));
