:christmas_tree:|:santa:|<img src='https://deno.com/images/artwork/HypnoDeno.gif?__frsh_c=dad2' width='15px' /> 
:-: | :- | :-
12  | Wildcard + 1D Nonogram           | DFS + Permutation w/ rules
11  | n(n-1)/2 Pairing                 | Keep only relevent coordinates 
10  | Graph                            | BFS + inside-a-polygon principle 
9   | Bruteforce  Sim                  | Append rows until row is all 0
8   | Iterate until it stops           | Lcm + and it will stop
7   | Wildcards + Poker                | Sorting w/ custiom comparator
6   | Quadratic equation               | Simply linear adding 
5   | Overlapping Intervals            | (1) `\|` (2) `\|` (3) 
||| left bound = max(curr & next L) 
||| right bound = min(curr & next R) 
4   | Math                             | Each child-win gains pts of parent that wins 
3   | Adjacent cells                   | Find ints around a '`*`'
|||`edgecase 1` end-of-row numbers
|||`edgecase 2` identical nums in 3x3
2   | String segment                   | Parse those strings
1   | Number words                     | Get number words

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
