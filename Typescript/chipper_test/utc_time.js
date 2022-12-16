/*
* make UTC DT
* make string of mock DB utc
* convert to date obj
* make offset of obj timezone offset method
* get MS time from conversion
* equation: time - offset * (60 * 60 * 60)
*
* call toISOstring()
* the INPUT was string
*
* DATE regular converts string to UTC
* DATE does not convert UTC string
*/
// const dateStr: string = '2022-05-21 04:00:29.056643'
var utcStr = '2022-05-21T04:00:29.334Z';
var dateUTC = new Date(utcStr);
console.log('My DT (utc) object is of type:');
console.log(typeof dateUTC);
console.log(dateUTC);
console.log("" + dateUTC);
// Here, we get
var weird = new Date('2022-05-21T04:00:29.334' + 'Z');
console.log('...weird:');
console.log("" + weird);
console.log();
/* in MILLISEC */
var milliTime = dateUTC.getTime();
console.log('My DT TIME object is of type:');
console.log(typeof milliTime);
console.log(milliTime);
console.log();
/* in MINUTES */
var offset = dateUTC.getTimezoneOffset();
console.log('My DT offset object is of type:');
console.log(typeof offset);
console.log(offset);
console.log();
/* convert offset (60 sec/min * 1k ms/sec )*/
var milliOffset = milliTime - offset * 60 * 1000;
console.log('My mil offset object is of type:');
console.log(typeof milliOffset);
console.log(milliOffset);
console.log();
/* convert back to string of UTC */
var newDtUTC = new Date(milliOffset).toISOString();
console.log('My new UTC str object is of type:');
console.log(typeof newDtUTC);
console.log("\toriginal utc date str: " + utcStr);
console.log("\tnew utc iso str:       " + newDtUTC);
console.log();
//const oneLiner = Date(utcStr) - Date(utcStr).getTimezoneOffset()
