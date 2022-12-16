"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const resolveAfter2Seconds = async () => {
    return new Promise(resolve => {
        setTimeout(() => {
            resolve('resolved');
        }, 2000);
    });
};
exports.asyncCall = async () => {
    console.log('calling');
    const result = await resolveAfter2Seconds();
    console.log(result);
    // expected output: "resolved"
};
exports.asyncCall();
//# sourceMappingURL=asAwait.js.map