F = 0
import functools, re
from collections import Counter
### 251473971 . 252357948 too lo
r1, r2 = 0, 0
A=[]
with open('07.' + str(F)) as file:
    for line in file:
        line=line.strip().split()
        L,R = line[0],line[1]
        counter=Counter(line[0])
        findmost = counter.most_common()
        #char = max(counter, key=counter.get)
        #paircount=counter[char]
        paircount=findmost[0][1]
        if paircount not in [4,5]:# 2 pair > 1 pair > Set
            if paircount == 3: # aaabb > aaabc
                if findmost[1][1] == 1:
                    paircount = 2
            elif paircount == 2:
                if findmost[1][1] == 1: # aabbc > aabcd
                    paircount = 0
                else:
                    paircount = 1
            elif paircount == 1:
                paircount = -1
        S,s=set(),''
        for c in L:
            if c not in S:
                S.add(c)
                s+=c
        line[0],line[1] = s, int(R)
        line.append(paircount)
        A.append(line)
print(A)
def cmp(ll, rr):
    l,r=ll[0],rr[0]
    c1,c2=ll[2],rr[2]
    if c1==c2:
        for a,b in zip([_ for _ in l], [_ for _ in r]):
            print(l,a,r,b, a>b)
            if ord(a) < ord(b):
                return 1
            elif ord(a) > ord(b):
                return -1
            else:
                continue
        return 0
    elif c1 > c2:
        return 1
    elif c1 < c2:
        return -1
    else:return 0
A.sort(key=functools.cmp_to_key(cmp))
for a in A:print(a)
for i in range(len(A)):
    r1 += A[i][1] * (i+1)
print(r1,r2)
