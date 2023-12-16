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
D = [((0, -1), (0, 1))] # top left moving right
#S.add((((0, -1), (0, 1))))
while D:
    curr, move = D.pop(0)
    r, c = curr
    r += move[0]
    c += move[1]
    if r < 0 or r > R - 1 or c < 0 or c > C - 1:
        continue
    curr = (r, c)
    t = A[r][c]
    if t == '.':# can skip
        coor = (curr, move)
        if coor not in S:
            D.append(coor)
            S.add(coor)
    elif t == '/':
        move = (-move[1], -move[0])
        coor = (curr, move)
        if coor not in S:
            D.append(coor)
            S.add(coor)
    elif t == '\\':
        move = (move[1], move[0])
        coor = (curr, move)
        if coor not in S:
            D.append(coor)
            S.add(coor)
    elif t == '-':
        if move[1] != 0:
            coor = (curr, move)
            if coor not in S:
                D.append(coor)
                S.add(coor)
        else: # split into 2 <--- moving horizontal
            move = (0, -1)
            coor = (curr, move)
            if coor not in S:
                D.append(coor)
                S.add(coor)
            move = (0, 1)
            coor = (curr, move)
            if coor not in S:
                D.append(coor)
                S.add(coor)
    elif t == '|':
        if move[0] != 0:
            coor = (curr, move)
            if coor not in S:
                D.append(coor)
                S.add(coor)
        else:
            move = (1, 0)
            coor = (curr, move)
            if coor not in S:
                D.append(coor)
                S.add(coor)
            move = (-1, 0)
            coor = (curr, move)
            if coor not in S:
                D.append(coor)
                S.add(coor)
SS = set()
SA = [_ for _ in S]
for p, _ in SA: 
    SS.add(p)

print(len(SS))

print("part 1:", r1)
print("part 2:", r2)

