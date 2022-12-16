"use strict";
const url = 'https://example.com';
// shorthand/high-level asychnronous
const asyncFunc = async (url) => {
    const { json } = await fetch(url);
    return 'mock';
};
// shorthand/high-level synchronous
const syncFunc = (url) => {
    // inner async return Promise
    const resPromise = new Promise((resolve, reject) => {
        resolve(fetch(url));
    });
    return resPromise;
};
asyncFunc(url);
//# sourceMappingURL=high_bad.js.map