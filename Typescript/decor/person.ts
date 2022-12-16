import { whoAmI } from "./decorators"


@whoAmI
class Person {
	constructor (private name: string, private age: number) {}
}
