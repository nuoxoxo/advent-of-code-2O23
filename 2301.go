package main

import (
    "fmt"
    "sort"
    "strconv"
    "strings"
)

const URL string = "https://adventofcode.com/2023/day/1/input"

var D = map[string]int{
    "one": 1, "two": 2, "three": 3,
    "four": 4, "five": 5, "six": 6,
    "seven": 7, "eight": 8, "nine": 9,
    "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,
}

func main () {
    lines := strings.Split((strings.TrimSpace(string(getbody(URL)))), "\n")
    res1, res2 := 0, 0
    for _, line := range lines {
        // part 1
        p1 := func(line string) int {
            var L, R byte
            for i := 0; i < len(line); i++ {
                if '0' <= line[i] && line[i] <= '9' {
                    L = line[i]
                    break
                }
            }
            for i := len(line) - 1; i > -1; i-- {
                if '0' <= line[i] && line[i] <= '9' {
                    R = line[i]
                    break
                }
            }
            res, _ := strconv.Atoi(string([]byte{L, R}))
            return res
        }

        // part 2
        p2 := func(line string) int {
            var a [][]int
            for k, v := range D {
                L := strings.Index(line, k)
                R := strings.LastIndex(line, k)
                if L != -1 { a = append(a, []int{L, v}) }
                if R != -1 { a = append(a, []int{R, v}) }
            }
            sort.Slice(a, func(l, r int)bool{ return a[l][0] < a[r][0] })
            L, R := strconv.Itoa(a[0][1]), strconv.Itoa(a[len(a) - 1][1])
            res, _ := strconv.Atoi(L + R)
            return res
        }

        res1 += p1(line)
        res2 += p2(line)
    }
    fmt.Println(YELL("part 1:"), res1)
    fmt.Println(YELL("part 2:"), res2)
    assert (res1 == 55208)
    assert (res2 == 54578)
}