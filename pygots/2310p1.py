F=0
r1, r2 = 0, 0
A=[]
sp = []
with open('10.' + str(F)) as file:
    for line in file:
        line=line.strip()
        A.append(line)
for a in A:print(a)
for r in range(len(A)):
    if 'S' in A[r]:
        for c in range(len(A[r])):
            if A[r][c] == 'S':
                sp.append((r,c))
assert(len(sp) == 1)
S = (sp[0][0],sp[0][1])
print('from:',sp)

# | - L J 7 F 
Go = ['J|L', '7|F', 'J-7', 'L-F'] # order : UDLR
Get= [Go[1], Go[0], Go[3], Go[2]]

D = [S]
seen = {S}
R, C = len(A), len(A[0])
print('seen:',seen)
print('bfs :',D)

dr=[-1, 1, 0, 0]
dc=[ 0, 0,-1, 1] # order : UDLR
while D:
    r, c = D.pop(0)
    pipcurr = A[r][c]
    for i in range(4):
        rr, cc = r + dr[i], c + dc[i]
        if (rr, cc) in seen or not (rr > -1 and rr < R and cc > -1 and cc < C):
            continue
        pipnext = A[rr][cc]
        #print('is legal move:', pipcurr, pipnext)
        if pipcurr in Go[i]+'S' and pipnext in Get[i]:
            seen.add((rr, cc))
            D.append((rr, cc))
print(seen)
r1 = len(seen) // 2

print('part 1:', r1)
print('part 2:', r2)

assert(r1 in [4,6947,6947*2])
