:christmas_tree:|:santa:|<img src='https://deno.com/images/artwork/HypnoDeno.gif?__frsh_c=dad2' width='15px' /> 
:-: | :- | :-
15  | Hashmap                          | `ordered map` `memorization` 
||
14  | Transpose a 2D List              | `2d transposition` 
||
13  | Wildcard + Transpose             | `2d transposition` `wildcard` 
||| ↳ The Wildcard has only 1 possible outcome
||
12  | 1D Nonogram                      | `wildcard`  `permutation` `recursive / DFS`
||| ↳ Guess wildcards to get max outcome
||| ↳ Permute inside a custom comparator
||| ↳ DFS 
||
11  | Coordinates Pairing              | Hard part 2 - `coordinates` `visualizing`
||| ↳ Keep only relevent coordinates 
||| ↳ n(n-1)/2 Pairing
||
10  | Graph                            | Hard problem - `BFS` 
||| ↳ BFS + inside-a-polygon principle 
||
9   | Bruteforce Sim                   | Medium
||| ↳ Append rows until row is all 0
||
8   | Iterate indefinitely             | Medium, a grid of states problem
||| ↳ Lcm + iterate until it stops 
||
7   | Wildcards + Poker                | Hard day 
||| ↳ Sorting hands w/ custiom comparator
||
6   | Quadratic equation               | Easy
||| ↳ linear adding 
||
5   | Intervals                        | Hard - `visualizing` `overlapping intervals`
||| ↳ ① `\|` ② `\|` ③ 
||| ↳ `max(curr & next L)` for L bound 
||| ↳ `min(curr & next R)` for R bound 
||
4   | Math                             | - Math is at the heart of part 2
||| ↳ Each child win gains pts of parent that wins 
||
3   | Parse djacent integers           | - Took me a while but a satisfying day 
||| ↳ Save a number by its begin, end coordinates
||| ↳ `edgecase 1` end-of-row numbers
||| ↳ `edgecase 2` identical nums in 3x3
||
2   | Parse sring segment              | - Reading comprehension  
||
1   | Parse number words               | - Reading comprehension  

>  [thread]: Also skoh, with the other problems you could create a map of the problem and then use that map to solve the problem. Here it's so big that you have to compare distances, instead of checking if the map at certain coordinates contains a certain character. This is what makes it harder - _Adringar 15/12/22_

&#8203;

![](https://i.imgur.com/xbrhMMC.png)

<!------------ FOOTNOTE ------------>

<!--

# &#8203;

Export session
```j
$ export AOC_SESSION=...
```

Python
- fetching: using `os.getenv` 

 Typescript
- HMR using Denon: run `denon start Filename.ts`
- non-watch mode: run `sh Deno.sh {1|2|...}`



Install Deno
```
✗ curl -fsSL https://deno.land/x/install/install.sh | sh
✗ which deno
✗ export AOC_SESSION=abc123
✗ printenv
✗ deno run --allow-read --allow-env --allow-net File.ts
```
Install Denon
```
✗ deno install --allow-read --allow-run -f https://deno.land/x/denon/denon.ts
✗ denon start File.ts
```
Write a denon.json
```
{
  "scripts": {
    "start": {
      "cmd": "deno run",
      "watch": true,
      "allow": ["read", "net", "env"],
      "ext": "ts",
      "unstable": true
    }
  }
}
```

-->

# :christmas_island: AOC

- [ ] todo : deploy 2214 - should be fun
- [ ] todo : 2214 dropping sand game in cc
- [ ] todo : 2211 monkeys' worry level in cc
- [ ] todo : deploy 2224 
- [x] _done_ : 2224 bfs in cc
- [x] _done_ : 1610 toposort in python

<img src='https://deno.com/images/artwork/hashrock_simple.png?__frsh_c=dad21828de649d12df5a23c572b88f3a3a73d0dc' width='13px' />|1|2|3|4|5|6|7|8|9|0
--|-|-|-|-|-|-|-|-|-|-
P |.|.|.|.|.|.|.|.|.|.
T |.|.| | |.| | | |.|
G |.|
C |.|.| | |.
| |1|2|3|4|5|6|7|8|9|0
P |.|.|.|.|.
T | |:
G | | | | |.
C |
| |1|2|3|4|5
P |
T |
G |
C |
