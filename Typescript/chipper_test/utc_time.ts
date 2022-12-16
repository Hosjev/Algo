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
const utcStr: string = '2022-05-21T04:00:29.334Z'
const dateUTC = new Date(utcStr)
console.log('My DT (utc) object is of type:')
console.log(typeof dateUTC)
console.log(dateUTC)
// Print execution freebie in locale time
console.log(`${dateUTC}`)
console.log()

/* in MILLISEC */
const milliTime = dateUTC.getTime()
console.log('My DT TIME object is of type:')
console.log(typeof milliTime)
console.log(milliTime)
console.log()

/* in MINUTES */
const offset = dateUTC.getTimezoneOffset()
console.log('My DT offset object is of type:')
console.log(typeof offset)
console.log(offset)
console.log()

/* convert offset (60 sec/min * 1k ms/sec )*/
const milliOffset = milliTime - offset * 60 * 1000
console.log('My mil offset object is of type:')
console.log(typeof milliOffset)
console.log(milliOffset)
console.log()

/* convert back to string of UTC */
const newDtUTC = new Date(milliOffset).toISOString()
console.log('My new UTC str object is of type:')
console.log(typeof newDtUTC)
console.log(`\toriginal utc date str: ${utcStr}`)
console.log(`\tnew utc iso str:       ${newDtUTC}`)
console.log()

//const oneLiner = Date(utcStr) - Date(utcStr).getTimezoneOffset()
