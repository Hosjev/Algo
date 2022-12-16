class Queue<T> {

  // public by default
  data = []

  // method name (args): RT
  push (item: T): void {
    this.data.push(item)
  }

  pop (): T {
    return this.data.shift()
  }
}


// num type and instantiate class object
const numsQ = new Queue<number>()
numsQ.push(1)
numsQ.push(2)
numsQ.push(3)
numsQ.push(4)
numsQ.push(5)
console.log(numsQ.pop())
console.log(numsQ.pop().toPrecision())

// num type and instantiate class object
const stringsQ = new Queue<string>()
stringsQ.push('foo')
stringsQ.push('bar')
stringsQ.push('bear')
stringsQ.push('zoo')
stringsQ.push('dump')
console.log(stringsQ.pop())
