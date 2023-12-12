let day = 12
import { config } from "https://deno.land/x/dotenv/mod.ts"
config()
let session = Deno.env.get("AOC_SESSION")

let get_stuff = (day): Promise<string> => {

  let url: string = `https://adventofcode.com/2023/day/${day}/input`
  console.log(session)
  let headers = new Headers({ 'Cookie': `session=${session}` })
  return fetch(url, { headers })
        .then((resp) => resp.text())
        .catch((err) => { throw err })
}

const DFS = (line:string, resource:number[]) => {

  if ( ! line || line === '' || [...line].every(c => c === '.')) {
    if (resource.length) {
      return 0
    }
    console.log('validated:', `"${line}"`)
    console.log('next rsce:',
      ! resource || resource.length < 1 ? [] : resource[0] + 
      `(in queue: ${resource.length - 1} other resources)`, '\n')
    return 1
  }
  if (line[0] === '?') {
    let OP = '.' + line.substring(1)
    let DM = '#' + line.substring(1)
    return DFS(OP, resource) + DFS(DM, resource)
  }
  if (line[0] === '#') {
    if (resource.length === 0) {
      return 0
    }
    let next_resource = resource[0]
    if (line.length < next_resource) {
      return 0
    }
    if ([...line.substring(0, next_resource)].some(c => c === '.')) {
      return 0
    }
    if (resource.length < 2) {
      return DFS(line.substring(next_resource), resource.slice(1))
    }
    if (resource.length > 1) {
      if (line.length < next_resource + 1) {
        return 0
      }
      if (line[next_resource] === '#') {
        return 0
      }
      console.log('will goto:', `"${line}"`)
      console.log('next rsce:',
        ! resource || resource.length < 1 ? [] : resource[0] + 
        ` (in queue: ${resource.length - 1} other resources)`, '\n')
      return DFS(line.substring(next_resource + 1), resource.slice(1))
    }
  }
  if (line[0] === '.') {
    return DFS(line.substring(1), resource)
  }
}

get_stuff(day).then((infile) => {

  let lines: string[] = infile.split('\n')
  lines.pop()
  let r1 = 0, r2 = 0
  for (let line of lines) {
    let [L, temp] = line.split(' ')
    let R = temp.split(',').map(Number)
    console.log(L, R)
    r1 += DFS(L, R)
  }

  console.log("part 1:", r1)
  console.log("part 2:", r2)

}).catch((err) => { throw err })

