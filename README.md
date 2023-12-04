:christmas_tree:|:santa:|<img src='https://deno.com/images/artwork/HypnoDeno.gif?__frsh_c=dad2' width='15px' /> 
:-: | :- | :-
4   | Mathy part 2   | each subseq win += pts of parent that wins
3   | Adjacent cells | Find ints around a '`*`'
||| Part 1 : might have used a wrong way 
|||`edgecase 1` end-of-row numbers
|||`edgecase 2` identical nums in 3x3
2   | String segment | should've used defaultdict
1   | Number words   | get number words

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
