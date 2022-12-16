var Dog = /** @class */ (function () {
    function Dog(name) {
        this.name = name;
    }
    Dog.prototype.sayHello = function (speak) {
        return this.name + " pup says " + speak;
    };
    return Dog;
}());
var Fish = /** @class */ (function () {
    function Fish(name) {
        this.name = name;
    }
    Fish.prototype.dive = function (deep) {
        return this.name + " fishy can dive " + deep + " feet deep";
    };
    return Fish;
}());
var talkToPet = function (pet) {
    if (pet instanceof Dog) {
        return pet.sayHello("bark");
    }
    else if (pet instanceof Fish) {
        return "Fishy can't speak";
    }
    return "pet instance not recognized";
};
var marie = new Dog("Marie");
var goldy = new Fish("Goldy");
console.log(talkToPet(marie));
console.log(talkToPet(goldy));
