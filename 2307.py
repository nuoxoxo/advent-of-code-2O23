import functools, re
from collections import Counter
F = 1
r1, r2 = 0, 0
A=[]
with open('07.' + str(F)) as file:
    for line in file:
        line=line.strip().split()
        L,R = line[0],line[1]
        ss=Counter(line[0])
        char = max(ss, key=ss.get)
        paircount=ss[char]
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
    L,R=set(l),set(r)
    if len(L)==len(R):
        for a,b in zip([_ for _ in l], [_ for _ in r]):
            print(l,a,r,b, a>b)
            if ord(a) > ord(b):
                return 1
            elif ord(a) < ord(b):
                return -1
            else:
                return 0
    elif len(L) < len(R):
        return 1
    elif len(L) > len(R):
        return -1
    return 0

A.sort(key=functools.cmp_to_key(cmp))
for a in A:print(a)
print(r1,r2)
