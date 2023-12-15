:christmas_tree:|:santa:|<img src='https://deno.com/images/artwork/HypnoDeno.gif?__frsh_c=dad2' width='15px' /> 
:-: | :- | :-
15  | Curiosly not graph               | `ordered map` `memorization` 
||
14  | Transpose a 2D List              | `2d transposition` 
||
13  | Wildcard + 2D Transpose          | `wildcard` 
||| ↳ Wildcard again but no guessing needed
||
12  | 1D Nonogram                      | `wildcard` 
||| ↳ DFS + Permutation w/ rules
||
11  | Coordinates Pairing              | - Hard time understanding part 2
||| ↳ Keep only relevent coordinates 
||| ↳ n(n-1)/2 Pairing
||
10  | Graph                            | - Hard
||| ↳ BFS + inside-a-polygon principle 
||
9   | Bruteforce Sim                   | - Medium
||| ↳ Append rows until row is all 0
||
8   | Iterate indefinitely             | - Medium, a grid of states problem
||| ↳ Lcm + iterate until it stops 
||
7   | Wildcards + Poker                | - Hard day 
||| ↳ Sorting hands w/ custiom comparator
||
6   | Quadratic equation               | - Simply 
||| ↳ linear adding 
||
5   | Intervals                        | - Hard day visualizing overlapping intervals
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
### todo : 1610 toposort

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
