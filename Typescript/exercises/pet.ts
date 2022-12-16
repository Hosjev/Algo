class Dog {
	constructor (readonly name: string) {}

	sayHello (speak: string): string {
	    return `${this.name} pup says ${speak}`
	}
}


class Fish {
	constructor (readonly name: string) {}

	dive (deep: string): string {
	    return `${this.name} fishy can dive ${deep} feet deep`
	}
}

type Pet = Dog | Fish

const talkToPet = (pet: Pet) => {
	if (pet instanceof Dog) {
		return pet.sayHello("bark")
	} else if (pet instanceof Fish) {
		return "Fishy can't speak"
	}
	return "pet instance not recognized"
}

const marie = new Dog("Marie")
const goldy = new Fish("Goldy")

console.log(talkToPet(marie))
console.log(talkToPet(goldy))
