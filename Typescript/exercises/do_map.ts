import { readFileSync, writeFileSync } from 'fs'
import { join } from 'path'

export function syncReadFile(dirname: string, filename: string) {
  return readFileSync(join(dirname, filename), 'utf-8')
}


const foo = JSON.parse(syncReadFile('/home/hosjev/Algo/Typescript/exercises', 'payload.json')).data[0]

console.log(foo.regions)

const bar = foo.regions.map((a) =>
    a.instances.map((b) =>
      b.ip
      )
    )
console.log(bar)
//instances is an array of objects
//const bar = JSON.parse(foo)
//const x = bar.data.regions.instances.map((a) => a.ip)
