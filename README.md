:christmas_tree:|:santa:|<img src='https://deno.com/images/artwork/HypnoDeno.gif?__frsh_c=dad2' width='15px' /> 
:-: | :- | :-
12  | Permutation + Wildcards | DFS + lru_cache
11  | `n(n-1)/2` Pairing | Keep only relevent coordinates 
10  | Graph             | BFS + inside-a-polygon principle 
9   | Brute Sim
8   | Iterate until it stops | Lcm 
7   | Poker + Wildcards 
6   | Quadratic equation| A simple lucky day
5   | Overlapping Intervals | `≈`max(lefts) `≈` min(rights) `≈`
||| instead of tracing every individual one
4   | Mathy part 2      | Each subseq win += pts of parent that wins
3   | Adjacent cells    | Find ints around a '`*`'
||| Part 1 : might have used a wrong way 
|||`edgecase 1` end-of-row numbers
|||`edgecase 2` identical nums in 3x3
2   | String segment    | Should've used defaultdict
1   | Number words      | Get number words

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
