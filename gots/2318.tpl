F = 0
r1, r2 = 0, 0
A = []
def dbg(T):
    for t in T:print(t)
from collections import defaultdict
with open('18.' + str(F)) as file:
    for line in file:
        A.append(line.strip())
curr=(0,0)
P={curr}
#V={curr}
#P=[curr]
V=[curr]
for a in A:
    d, n, line = a.split()
    n=int(n)
    r,c = [*curr]
    if d == 'R':
        for i in range(n+1):
            P.add((r, c+i))
            #P.append((r, c+i))
        c+=n
    elif d == 'D':
        for i in range(n+1):
            #P.append((r+i,c))
            P.add((r+i,c))
        r+=n
    elif d == 'L':
        for i in range(n+1):
            P.add((r,c-i))
            #P.append((r,c-i))
        c-=n
    elif d == 'U':
        for i in range(n+1):
            P.add((r-i,c))
            #P.append((r-i,c))
        r-=n
    curr = (r,c)
    V.append(curr)
    #V.add(curr)
#D=list(V)
D=V
# shoelace
# way3
up,down=0,0
for i in range(len(D) - 1):
    up = up + D[i][0] * D[i+1][1]
    down = down + D[i][1] * D[i+1][0]
up += D[-1][0] * D[0][1]
down += D[0][0] * D[-1][1]
area = abs(up - down) // 2
peri = len(P)
pick = area - peri // 2  + 1
r1 = res = peri + pick

print(V)
print('sizeof vtc:',len(V),'should be: 14 or 15')
print('sizeof pts:',len(P),'should be:',38)
print(P)
print('way 3 full area:',area)
print('way 3 perimeter:',peri)
print('way 3 pick fact:',pick)
print('way 3 true area:',res)

# part 2

DIR = ['R','D','L','U']
curr=(0,0)
P={curr} # no need
#V={curr}
#P=[curr]
V=[curr]
peri = 0
for a in A:
    l, n, line = a.split()
    Hex = line[2:7]
    
    d = DIR[int(line[-2])]
    n = int(Hex, 16)
    #print(d, n)
    r,c = [*curr]
    if d == 'R':
        c+=n
    elif d == 'D':
        r+=n
    elif d == 'L':
        c-=n
    elif d == 'U':
        r-=n
    curr = (r,c)
    V.append(curr)
    peri += n
D=V
up,down=0,0
for i in range(len(D) - 1):
    up = up + D[i][0] * D[i+1][1]
    down = down + D[i][1] * D[i+1][0]
up += D[-1][0] * D[0][1]
down += D[0][0] * D[-1][1]
area = abs(up - down) // 2
# peri = len(P)
pick = area - peri // 2  + 1
r2 = res = peri + pick
print("part 1:", r1)
print("part 2:", r2)
