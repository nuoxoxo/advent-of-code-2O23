F = 0
r1, r2 = 0, 0
A = []
def dbg(T):
    for t in T:print(' '.join(t))
    print()
with open('16.' + str(F)) as file:
    for line in file:
        A.append([_ for _ in line.strip()])
print(A)
R, C = len(A), len(A[0])
S = set()
#D = [((0, -1), (0, 1))] # top left moving right
#S.add((((0, -1), (0, 1))))
def BFS(A, curr, move) -> int:
    R, C = len(A), len(A[0])
    S = set()
    D = [(curr, move)] # top left moving right
    while D:
        curr, move = D.pop(0)
        r, c = curr
        r += move[0]
        c += move[1]
        if r < 0 or r > R - 1 or c < 0 or c > C - 1:
            continue
        curr = (r, c)
        t = A[r][c]
        todo = []
        if t == '.':# can skip
            coor = (curr, move)
            todo.append(coor)
        elif t == '/':
            move = (-move[1], -move[0])
            coor = (curr, move)
            todo.append(coor)
        elif t == '\\':
            move = (move[1], move[0])
            coor = (curr, move)
            todo.append(coor)
        elif t == '-':
            if move[1] != 0:
                coor = (curr, move)
                todo.append(coor)
            else: # split into 2 <--- moving horizontal
                move = (0, -1)
                coor = (curr, move)
                todo.append(coor)
                move = (0, 1)
                coor = (curr, move)
                todo.append(coor)
        elif t == '|':
            if move[0] != 0:
                coor = (curr, move)
                todo.append(coor)
            else:
                move = (1, 0)
                coor = (curr, move)
                todo.append(coor)
                move = (-1, 0)
                coor = (curr, move)
                todo.append(coor)
        for job in todo:
            if job in S: continue
            D.append(job)
            S.add(job)
    SS = set()
    for p, _ in S:
        SS.add(p)
    return len(SS)
r1 = BFS(A, (0, -1),(0,1))
for r in range(R):
    r2 = max(r2, BFS(A, (r, -1), (0,  1)))
    r2 = max(r2, BFS(A, (r,  C), (0, -1)))
for c in range(C):
    r2 = max(r2, BFS(A, (-1, c), ( 1, 0)))
    r2 = max(r2, BFS(A, ( R, c), (-1, 0)))
print("part 1:", r1)
print("part 2:", r2)


