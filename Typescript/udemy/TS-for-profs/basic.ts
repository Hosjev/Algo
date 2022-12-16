const a: Array<number> = [1,2,3,4,5]

// name func = (args): returnType => {enter the function logic}
const sum = (...vals: Array<number>): number => {
  return vals.reduce((p, c) => {
    return p+c
  })
}

console.log(a)
console.log(sum(3,4,5))
