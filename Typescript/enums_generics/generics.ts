interface IntComparator<T> {
	compareTo(value: T | any): number
}

class Rect implements IntComparator<Rect> {

	constructor (private width: number, private height: number) {}

	compareTo(value: Rect): number {
		return (this.width * this.height) - (value.width * value.height)
	}
}

class Triangle implements IntComparator<Triangle> {

	constructor (private width: number, private height: number) {}

	compareTo(value: Triangle): number {
		return this.width * this.height - value.width * value.height
	}
}


const rec2: Rect = new Rect(3,5)
const rec1: Rect = new Rect(2,4)
const diff = rec1.compareTo(rec2)

/* LOGIC */
diff > 0 ? console.log(`Rect1 is bigger in area than 2 by: ${diff}`) :
	diff == 0 ? console.log('Rect1 is same as 2') :
	console.log(`Rect1 is smaller in area than 2 by: ${Math.abs(diff)}`)
