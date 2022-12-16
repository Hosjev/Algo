const url = 'https://example.com'


// shorthand/high-level asychnronous
const asyncFunc = async (url: string): Promise<string> => {
	const { json } = await fetch(url)
	return 'mock'
}

// shorthand/high-level synchronous
const syncFunc = (url: string): object => {
	// inner async return Promise
	const resPromise = new Promise((resolve, reject) => {
		resolve(fetch(url))
	})
	return resPromise
}

asyncFunc(url)
