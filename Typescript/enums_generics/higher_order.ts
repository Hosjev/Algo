/*
* Generic function to return a signature
* @<T> = generic type
* returns (c: number) ? number
*/
type numFunc<T> = (arg: T) => (c: number) => number

/*
* Invokes function with no argument
*/
const noArgFunc: numFunc<void> = () => (c: number) => c + 5

/*
* Invokes function with argument
*/
const numArgFunc: numFunc<number> = (val: number) => (other_val: number) => val * other_val

/*
* Invokes function with string argument
*/
const numStrFunc: numFunc<string> = (val: string) => (other_val: number) => val.length * other_val

const noArg = noArgFunc()
console.log(noArg(5))
