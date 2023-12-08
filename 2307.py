F = 0
import functools, re
from collections import Counter
### 251473971 . 252357948 too lo .. 252348193 x
r1, r2 = 0, 0
A,E=[],[]
with open('07.' + str(F)) as file:
    for line in file:
        line=line.strip().split()
        L,R = line[0],line[1]
        E.append((L,R))
        L = L.replace('A','|')\
            .replace('K','_')\
            .replace('Q','^')\
            .replace('J',']')\
            .replace('T','[') # can make a func
        line[0] = L
        counter = Counter(line[0])
        findmost = counter.most_common()
        paircount = findmost[0][1]
        if paircount not in [4,5]:# 2 pair > 1 pair > Set
            if paircount == 3: # aaabb > aaabc
                if findmost[1][1] == 2:
                    paircount = 3 # aaabb
                elif findmost[1][1] == 1:
                    paircount = 2 # aaabc
            elif paircount == 2:
                if findmost[1][1] == 2: # aabbc > aabcd
                    paircount = 1 # aabbc
                else:
                    paircount = 0 # aabcd
            elif paircount == 1:
                paircount = -1 # floor: all uniq
        S, s = set(), ''
        for c in L:
            if c not in S:
                S.add(c)
                s+=c # wrong? to rev later
        line[1] = int(R)
        line.append(paircount)
        A.append(line)

def dbg(A):
    for a in A:print(a)

def cmp(ll, rr):
    l,r=ll[0],rr[0]
    c1,c2=ll[2],rr[2]
    if c1==c2:
        for a,b in zip([_ for _ in l], [_ for _ in r]):
            if ord(a) > ord(b):return 1
            elif ord(a) < ord(b):return -1
        return 0
    return (c1 > c2) - (c1 < c2)
    """elif c1 > c2: return 1
    elif c1 < c2: return -1
    return 0
    """
A.sort(key=functools.cmp_to_key(cmp))
for i in range(len(A)): r1 += A[i][1] * (i + 1)
dbg(E)#A)
print('part 1:', r1)

# part 2 - deprecated
cardtypes=[] # fill with all card types
BB,B=A.copy(),[] # for part 2
"""deprecated
for line in B:
    print(line)
    b = []
    s,pts,=line
    if ']' not in s:
        b.append(line)
        B.append(b)
        continue
    for ct in cardtypes:
        ss=s.replace(']', ct)
        b.append([ss, pts])
    # ^ i think thats it
    # todo: use cmp logic to a sorted subgroup
    # keep the best ie. top of the sorted subg
for b in B:
    b[0].sort(key=functools.cmp_to_key(cmp))
    b[0]=b[0][0]

A.sort(key=functools.cmp_to_key(cmp))
B.sort(key=functools.cmp_to_key(cmp))
for a in A:print(a)
for i in range(len(A)):
    r1 += A[i][1] * (i+1)
for i in range(len(B)):
    r2 += B[i][1] * (i+1)
print(r1,r2)
"""
