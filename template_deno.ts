const day = 1

import { config } from "https://deno.land/x/dotenv/mod.ts"

config()
let session = Deno.env.get("AOC_SESSION")

//  the deno way : Promise w/o async-await

const fetch_input = (day: number): Promise<string> => {

    let url: string = `https://adventofcode.com/2022/day/${day}/input`
    const headers = new Headers({ 'Cookie': `session=${session}` })

    return fetch(url, { headers })
        .then ((resp) => resp.text())
        .catch ((err) => { throw err })
}

fetch_input(day).then((infile) => {

    console.log(infile)

    // solution
    console.log('part 1:')
    console.log('part 2:')

}).catch((err) => { throw err })

