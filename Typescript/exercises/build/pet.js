"use strict";
class Dog {
    constructor(name) {
        this.name = name;
    }
    sayHello(speak) {
        return `${this.name} pup says ${speak}`;
    }
}
class Fish {
    constructor(name) {
        this.name = name;
    }
    dive(deep) {
        return `${this.name} fishy can dive ${deep} feet deep`;
    }
}
const talkToPet = (pet) => {
    if (pet instanceof Dog) {
        return pet.sayHello("bark");
    }
    else if (pet instanceof Fish) {
        return "Fishy can't speak";
    }
    return "pet instance not recognized";
};
const marie = new Dog("Marie");
const goldy = new Fish("Goldy");
console.log(talkToPet(marie));
console.log(talkToPet(goldy));
//# sourceMappingURL=pet.js.map