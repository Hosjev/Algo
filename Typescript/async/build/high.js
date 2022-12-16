"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const node_fetch_1 = require("node-fetch");
//const url = 'https://dummy.restapiexample.com/api/v1/employees'
const url = 'https://jsonplaceholder.typicode.com/todos/1';
// Implementation code where T is the returned data shape
const api = async (url) => {
    // Run this async function, immediately handle Promise resolve and reject
    return node_fetch_1.default(url)
        .then(response => {
        if (!response.ok) {
            console.log(response);
            throw new Error(response.statusText);
        }
        return response.json();
    })
        .catch((error) => {
        //console.log('api error: ' + error)
        throw new Error(error);
    });
};
// Callback
// write a function to process callback, replace 2nd chain
// Consumer
exports.run = async () => {
    return api(url)
        .then((data) => {
        return Promise.resolve(data);
    })
        .then(value => {
        return value;
    })
        .catch(error => {
        /* show error message */
        console.log('run error: ' + error);
        //throw new Error(error)
    });
};
//# sourceMappingURL=high.js.map