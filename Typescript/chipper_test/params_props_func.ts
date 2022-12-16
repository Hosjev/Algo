/*
* Type checking IS done on arguments
* (the non-explicit passing of 'argument name'
*  that happens to match what's in the object evals to true)
* The above statement is TRUE in the Chipper stack, not here
* *the point here is that type checking IS done
*/

enum Currency {
	USD = 'USDollar'
}

export function money(opts: {
	currency: Currency | string
	amount: number | string
}): string {
	/* do stuff, return thing */
	return `${opts.amount} ${opts.currency}`
}

const myCurr: Currency = Currency.USD
const myAmt: number = 3

const result: string = money({
	currency: myCurr,
	amount: myAmt,
})

console.log(`print this hotmess: ${result}`)
