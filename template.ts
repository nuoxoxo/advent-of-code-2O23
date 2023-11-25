const day = 1

import * as dotenv from 'dotenv'
import axios from 'axios'

dotenv.config()
let session = process.env.AOC_SESSION

let fetch_input = async (day: number) : Promise<string> => {

    let url: string = `https://adventofcode.com/2022/day/${day}/input`
    let headers = { 'Cookie': `session=${session}` }
    try {
        return await axios.get(url, { headers })
    } catch (err) { throw err }
}

fetch_input(day).then( (infile) => {

    let lines = infile['data'].split('\n\n').map((bloc) => {
        return bloc.split('\n').map(Number)
    })
    let sums = lines.map((bloc) => {
        return bloc.reduce((a, c) => a + c, 0)
    })
    console.log('part 1:', Math.max(...sums))
    sums.sort((a, b) => b - a)
    let top3 = sums[0] + sums[1] + sums[2]
    console.log('part 2:', top3)

}).catch ((err) => { throw err })

