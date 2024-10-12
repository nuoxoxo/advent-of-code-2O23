package main

import (
    "net/http"
    "io/ioutil"
    "fmt"
    "os"
    "sort"
    "strconv"
    "strings"
)

var D map[string]int = map[string]int{
    "one": 1, "two": 2, "three": 3,
    "four": 4, "five": 5, "six": 6,
    "seven": 7, "eight": 8, "nine": 9,
    "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,
}

func main () {
    URL := "https://adventofcode.com/2023/day/1/input"
    lines := strings.Split((strings.TrimSpace(string(getbody(URL)))), "\n")
    res1, res2 := 0, 0

    for _, s := range lines {
        var L, R byte
        for i := 0; i < len(s); i++ {
            if '0' <= s[i] && s[i] <= '9' {
                L = s[i]
                break
            }
        }
        for i := len(s) - 1; i > -1; i-- {
            if '0' <= s[i] && s[i] <= '9' {
                R = s[i]
                break
            }
        }
        n, _ := strconv.Atoi( string([]byte{L, R}) )
        res1 += n

        // part 2
        var a [][]int
        for k, v := range D {
            l := strings.Index(s, k)
            r := strings.LastIndex(s, k)
            if l != -1 {
                a = append(a, []int{l, v})
            }
            if r != -1 {
                a = append(a, []int{r, v})
            }
        }
        sort.Slice(a, func(x, y int)bool{ return a[x][0] < a[y][0] })
        ll := strconv.Itoa(a[0][1])
        rr := strconv.Itoa(a[len(a) - 1][1])
        n, _ = strconv.Atoi(ll + rr)
        res2 += n
    }
    fmt.Println(YELL("part 1:"), res1)
    fmt.Println(YELL("part 2:"), res2)
}

func getbody(URL string) []uint8 {
    session_value := os.Getenv("COOK")
    if session_value == "" {
        panic("session/empty")
    }
    conn := &http.Client {}
    req, _ := http.NewRequest("GET", URL, nil)
    session := &http.Cookie {
        Name:   "session",
        Value:  session_value,
    }
    req.AddCookie( session )
    resp, _ := conn.Do(req)
    defer resp.Body.Close()
    body, _ := ioutil.ReadAll(resp.Body)
    return body
}

func assert(expression bool) {
    if ! expression {
        fmt.Print(YELL("assert/false "))
        panic(expression)
    }
}

const Yell, Cyan, Rest string = "\033[33m", "\033[36m", "\033[0m"
func YELL(s string)string{ return Yell + s + Rest }
func CYAN(s string)string{ return Cyan + s + Rest }

