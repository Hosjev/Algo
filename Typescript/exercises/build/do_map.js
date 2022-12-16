"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const fs_1 = require("fs");
const path_1 = require("path");
function syncReadFile(dirname, filename) {
    return fs_1.readFileSync(path_1.join(dirname, filename), 'utf-8');
}
exports.syncReadFile = syncReadFile;
const foo = JSON.parse(syncReadFile('/home/hosjev/Algo/Typescript/exercises', 'payload.json')).data[0];
console.log(foo.regions);
const bar = foo.regions.map((a) => a.instances.map((b) => b.ip));
console.log(bar);
//instances is an array of objects
//const bar = JSON.parse(foo)
//const x = bar.data.regions.instances.map((a) => a.ip)
//# sourceMappingURL=do_map.js.map