package main

import (
    "fmt"
    "strings"
    "strconv"
)

const URL string = "https://adventofcode.com/2023/day/2/input"
var D = map[string]int{ "red": 12, "blue": 14, "green": 13, }

func main() {
    res1, res2 := 0, 0
    idx := 1
    lines := strings.Split((strings.TrimSpace(string(getbody(URL)))), "\n")
    for _, line := range lines {
        temp := strings.Split(line, ":")[1]
        words := strings.Split(temp, ";")
        ok := true // part 1
        R, G, B := 0, 0, 0 // part 2
        for _, w := range words {
            sub := strings.Split(w, " ")[1:]
            for i := 0; i < len(sub) - 1; i += 2 {
                number, color := sub[i], sub[i + 1]
                if color[len(color) - 1] == ',' {
                    color = color[ : len(color) - 1]
                }
                n, _ := strconv.Atoi( number )
                // part 1
                if n > D[color] { ok = false }
                // part 2
                if color == "red" { R = max(R, n) }
                if color == "blue" { B = max(B, n) }
                if color == "green" { G = max(G, n) }
            }
        }
        // part 1
        if ok { res1 += idx }
        // part 2
        res2 += R * B * G
        idx += 1
    }
    fmt.Println(YELL("part 1:"), res1)
    fmt.Println(YELL("part 2:"), res2)
    assert (res1 == 2085)
    assert (res2 == 79315)
}

