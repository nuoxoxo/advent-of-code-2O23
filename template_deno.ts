const day = 1

import { config } from "https://deno.land/x/dotenv/mod.ts"

config()
let session = Deno.env.get("AOC_SESSION")

const fetch_input = async (day: number): Promise<string> => {

    let url: string = `https://adventofcode.com/2022/day/${day}/input`
        const headers = new Headers({ 'Cookie': `session=${session}` })
    try {
        let resp = await fetch(url, { headers })
        return await resp.text()
    } catch (err) { throw err }
}

fetch_input(day).then((infile) => {

    let lines = infile.split('\n\n').map((bloc) => {
        return bloc.split('\n').map(Number)
    })
    let sums = lines.map((bloc) => {
        return bloc.reduce((a, c) => a + c, 0)
    })
    console.log('part 1:', Math.max(...sums))
    sums.sort((a, b) => b - a)
    let top3 = sums[0] + sums[1] + sums[2]
    console.log('part 2:', top3)

}).catch((err) => { throw err })

