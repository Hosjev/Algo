"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
// Our upstream caller
async function primaryFunction() {
    const answer = await secondaryFunctionNull();
    // if answer is true
    if (answer) {
        // resolving
        console.log(`the answer is: ${answer}`);
        console.log(`the answer is of type: ${typeof answer}`);
        throw new Error('I am throwing an error to the upstream caller');
    }
    // resolving
    console.log(`the answer is: ${answer}`);
    console.log(`the answer is of type: ${typeof answer}`);
}
exports.primaryFunction = primaryFunction;
// Does this function EXPLICITLY return false (the data type)
//  or null (data type) according to the catch
// this function always returns the type boolean
async function secondaryFunction() {
    try {
        const foo = false;
        return foo;
    }
    catch (err) {
        console.log('An exception was thrown');
        return false;
    }
}
// this function returns null depending on the answer
async function secondaryFunctionNull() {
    try {
        const foo = false;
        if (foo) {
            return foo;
        }
    }
    catch (err) {
        console.log('An exception was thrown in null');
        return false;
    }
}
//# sourceMappingURL=exper1.js.map