# Perks of Go

&#8203;| &#8203;
:-     | :-
&#8203;| _- Atoi . Itoa -_
go     | <kbd>i, err := strconv.Atoi("-42")</kbd>
go     | <kbd>s := strconv.Itoa(-42)</kbd>
||
&#8203;| _- Sort an int array -_
ts     | `nums.sort((a, b) => a - b)`
py     | `nums.sort()`
go     | <kbd>sort.Ints(nums)</kbd>
||
&#8203;| _- Make a dict/map -_
go     | <kbd>E := make( map[ *Node ] *Node )</kbd>
py     | `E = defaultdict(lambda: None)`
cc     | `map<Node*, Node*> E`
||
&#8203;| _- Make a pointer -_
cc     | `ListNode *prev = nullptr`
go     | <kbd>prev := (*ListNode)(nil)</kbd>
||
&#8203;| _- Make an array or a 2D grid -_
cc     | `vector<ListNode*> arr`
go     | <kbd>res := make([]*ListNode, 0)</kbd>
||
cc     | `vector<vector<int>> grid`
go     | <kbd>var grid [][]int</kbd>
&#8203;| <kbd>grid := make([][]int, 0)</kbd>
||
cc     | `vector<int> arr(k, 0)`
go     | <kbd>arr := make([]int, k)</kbd>
