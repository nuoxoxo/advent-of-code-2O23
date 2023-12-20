:christmas_tree:|:santa:|<img src='https://deno.com/images/artwork/HypnoDeno.gif?__frsh_c=dad2' width='15px' /> 
:-: | :- | :- 
19  | Toposort                         | Hard one 
||| - _no idea for part2_
19  | Toposort                         | Hard one - `interval` for the 2nd part `BFS` 
||| - difficult part 2
||
18  | Polygon                          | Hard problem - `shoelace algorithm` `pick theorem`
||
17  | Dijkstra                         | `priority queue` `heapq` `dijkstra`
||| - cf. 2021/day/15 
||
16  | BFS                              | Bruteforce traversal under rules
|| 
15  | Hashmap                          | `ordered map implementation` `memorization` 
||| - Biggest pb is in reading comprehension 
||
14  | Transpose a 2D List              | `2d transposition` 
||
13  | Wildcard + Transpose             | `2d transposition` `wildcard` 
||| - The Wildcard has only 1 possible outcome 
||
12  | 1D Nonogram                      | `wildcard`  `permutation` `recursive / DFS`
||| - Guess wildcards to get max outcome 
||| - Permute inside a custom comparator 
||| - DFS 
||
11  | Coordinates Pairing[^Grid]       | Hard part 2 - `coordinates` `visualizing`
||| - Keep only relevent coordinates 
||| - n(n-1)/2 Pairing 
||
10  | Polygon + Graph                  | Hard problem - `BFS` 
||| - BFS + inside-a-polygon principle 
||
9   | Bruteforce Sim                   | Medium
||| - Append rows until row is all 0
||
8   | Iterate indefinitely             | Medium, a grid of states problem
||| - Lcm + iterate until it stops 
||
7   | Wildcards + Poker                | Hard day 
||| - Sorting hands w/ custiom comparator
||
6   | Quadratic equation               | Easy
||| - linear adding 
||
5   | Intervals                        | Hard - `visualizing` `overlapping intervals`
||| - ① `\|` ② `\|` ③ 
||| - `max(curr & next L)` for L bound 
||| - `min(curr & next R)` for R bound 
||
4   | Math                             | - Math is at the heart of part 2
||| - Each child win gains pts of parent that wins 
||
3   | Parse djacent integers           | - Took me a while but a satisfying day 
||| - Save a number by its begin, end coordinates
||| - `edgecase 1` end-of-row numbers
||| - `edgecase 2` identical nums in 3x3
||
2   | Parse sring segment              | - Reading comprehension  
||
1   | Parse number words               | - Reading comprehension  

<!------------ FOOTNOTE ------------>

[^Grid]:
    [thread]: Also skoh, with the other problems you could create a map of the problem and then use that map to solve the problem. Here it's so big that you have to compare distances, instead of checking if the map at certain coordinates contains a certain character. This is what makes it harder - _Adringar 15/12/22_

<!-- ![](https://i.imgur.com/xbrhMMC.png) -->

