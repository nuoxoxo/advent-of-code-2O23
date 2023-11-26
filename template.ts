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

    console.log(infile)
    console.log('part 1:')
    console.log('part 2:')

}).catch ((err) => { throw err })

