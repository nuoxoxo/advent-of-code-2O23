F = 0
from collections import defaultdict 
r1, r2 = 0, 0
A,sds=[],[]
D=[]
with open('05.' + str(F)) as file:
    tmp = []
    for line in file:
        line=line.strip()
        if 'seeds' in line:
            sds = [int(_) for _ in line.split(':')[1].split()]
            continue
        if not line and tmp:
            A.append(tmp)
            tmp = []
            continue
        if line: tmp.append(line)
    A.append(tmp)
for a in A:
    tmp = [_.split() for _ in a[1:]]
    temp = []
    for r in tmp:
        r.reverse()
        rr = [int(_) for _ in r]
        temp.append(rr)
    D.append(temp)
#for _ in D:print(_)
#print()
for d in D:
    for i in range(len(sds)):
        sd = sds[i]
        found = False
        for size, begin, end in d:
            if sd in range(begin, begin + size):
                found = True
                goto = sd - begin + end
                sds[i] = goto
                break
print("part 1:", min(sds))
print("part 2:", r2)
