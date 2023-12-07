F = 0
import functools, re
from collections import Counter
### 251473971 . 252357948 too lo .. 252348193 x
r1, r2 = 0, 0
A=[]
with open('07.' + str(F)) as file:
    for line in file:
        line=line.strip().split()
        L,R = line[0],line[1]
        L=L.replace('A','|').replace('K','_').replace('Q','^').replace('J',']').replace('T','[')
        line[0] = L
        counter=Counter(line[0])
        findmost = counter.most_common()
        pc=findmost[0][1]
        if pc not in [4,5]:# 2 pair > 1 pair > Set
            if pc == 3: # aaabb > aaabc
                if findmost[1][1] == 2:
                    pc = 3 # aaabb
                elif findmost[1][1] == 1:
                    pc = 2 # aaabc
            elif pc == 2:
                if findmost[1][1] == 2: # aabbc > aabcd
                    pc = 1 # aabbc
                else:
                    pc = 0 # aabcd
            elif pc == 1:
                pc = -1 # last : all uniq
        S,s=set(),''
        for c in L:
            if c not in S:
                S.add(c)
                s+=c # wrong? to fix later
        line[0],line[1] = L, int(R)
        line.append(pc)
        A.append(line)

BB,B=A.copy(),[] # for part 2

# part 2
cardtypes=[] # fill with all card types
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


# part 1
def cmp(ll, rr):
    l,r=ll[0],rr[0]
    c1,c2=ll[2],rr[2]
    if c1==c2:
        for a,b in zip([_ for _ in l], [_ for _ in r]):
            print(l,a,r,b, a>b)
            if ord(a) > ord(b):
                return 1
            elif ord(a) < ord(b):
                return -1
        return 0
    elif c1 > c2:
        return 1
    elif c1 < c2:
        return -1
    return 0

A.sort(key=functools.cmp_to_key(cmp))
B.sort(key=functools.cmp_to_key(cmp))
for a in A:print(a)
for i in range(len(A)):
    r1 += A[i][1] * (i+1)
for i in range(len(B)):
    r2 += B[i][1] * (i+1)
print(r1,r2)

