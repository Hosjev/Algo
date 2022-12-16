const resolveAfter2Seconds = async () => {
  return new Promise(resolve => {
    setTimeout(() => {
      resolve('resolved');
    }, 2000)
  })
}

export const asyncCall = async () => {
  console.log('calling');
  const result = await resolveAfter2Seconds();
  console.log(result);
  // expected output: "resolved"
}

asyncCall()
