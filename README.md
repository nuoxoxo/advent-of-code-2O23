# Todo
- _py : boilerplate - try fetching . try reading env var_
- _cc : Makefile - to prepare from last year_
- _ts : boilerplate - for quick compilation_


# Perks of Go

&#8203;| &#8203;
:-     | :-
&#8203;| _- Atoi . Itoa -_
go     | <kbd>i, err := strconv.Atoi("-42")</kbd>
go     | <kbd>s := strconv.Itoa(-42)</kbd>
||
&#8203;| _- Sort an int array -_
ts     | `nums.sort((a, b) => a - b)`
go     | <kbd>sort.Ints(nums)</kbd>
||
&#8203;| _- Make a dict/map -_
go     | <kbd>E := make( map[ *Node ] *Node )</kbd>
py     | `E = defaultdict(lambda: None)`
cc     | `map<Node*, Node*> E`
||
|| _- Make a pointer -_
cc     | `ListNode *prev = nullptr`
go     | <kbd>prev := (*ListNode)(nil)</kbd>
||
|| _- Make an array -_ 
cc     | `vector<ListNode*> arr`
go     | <kbd>res := make([]*ListNode, 0)</kbd>
||
cc     | `vector<int> arr(k, 0)`
go     | <kbd>arr := make([]int, k)</kbd>
||
|| _- Make a 2D grid -_ 
cc     | `vector<vector<int>> grid`
go     | <kbd>var grid [][]int</kbd>
&#8203;| <kbd>grid := make([][]int, 0)</kbd>


### PY
_Reading data_
```py
infile = _
from helpers.reader import read_as_list
suffix = '1804.' + str(infile)
lines = read_as_list( suffix )
lines.pop()
```
_Thingy_
```py
defaultdict(lambda: 0)
defaultdict(int)
```
### TS
_To Start with_
```ts
$ npm i --save-dev @types/node
$ npm install axios

// Run .ts with
$(camp) npx && node 
$(home) tsx && node
```
_Reading data_
```go
const choice = 0
const axios = require('axios')
const url = 'https://raw.githubusercontent.com/nuoxoxo/in/main/aoc/180█.' + choice.toString();

(async () => {

    try {
        const resp = await axios.get( url )
        const lines = resp.data.split('\n')
        console.log(resp)
        console.log(lines)
    } catch (e) {
        console.log('error - ', e)
    }
})()
```
_Thingy_
```go
...
D[id] = D[id] ? D[id] + 1 : 1
D[id] = ( D[id] || 1 ) + 1
...
// In a JavaScript/TypeScript for...in loop to iterate
// over the properties of an object, 
// the loop variable is always a string even if
// the keys in the object are numbers
```
