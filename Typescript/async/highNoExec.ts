import fetch from 'node-fetch'


//const url = 'https://dummy.restapiexample.com/api/v1/employees'
const url = 'https://jsonplaceholder.typicode.com/todos/1'

// Implementation code where T is the returned data shape
const api = async (url: string): Promise<string> => {    
  // Run this async function, immediately handle Promise resolve and reject
  return fetch(url)
      .then(response => {
        if (!response.ok) {
          console.log(response)
          throw new Error(response.statusText)
        }
        return response.json()
      })
      .catch((error) => {
        //console.log('api error: ' + error)
	throw new Error(error)
      })
  
}
  
const resolveRun = (data) => {
  console.log('resolved: ', data)
}

// Consumer
export const run = async () => {
  return api(url)
    .then((data: any) => {
      // explicit resolve, BUT it returns a thenable
      //return Promise.resolve(data)
      resolveRun(data)
    })
    .catch(error => {
      /* show error message */
      console.log('run error: ' + error)
      //throw new Error(error)
    })
}

run()
