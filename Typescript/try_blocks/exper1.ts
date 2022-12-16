// Our upstream caller
export async function primaryFunction() {
  const answer = await secondaryFunctionNull()
  // if answer is true
  if (answer) {
    // resolving
    console.log(`the answer is: ${answer}`)
    console.log(`the answer is of type: ${typeof answer}`)
    throw new Error('I am throwing an error to the upstream caller')
  }
  // resolving
  console.log(`the answer is: ${answer}`)
  console.log(`the answer is of type: ${typeof answer}`)
}


// Does this function EXPLICITLY return false (the data type)
//  or null (data type) according to the catch

// this function always returns the type boolean
async function secondaryFunction(): Promise<boolean> {
  try {
    const foo = false
    return foo
  } catch (err) {
    console.log('An exception was thrown')
    return false
  }
}

// this function returns null depending on the answer
async function secondaryFunctionNull(): Promise<boolean> {
  try {
    const foo = false
    if (foo) {
      return foo
    }
  } catch (err) {
    console.log('An exception was thrown in null')
    return false
  }
}

