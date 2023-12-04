from collections import defaultdict 
F = 0
r1, r2 = 0, 0
A=[]
D={}
d=defaultdict(int)
with open('04.' + str(F)) as file:
    for line in file:
        line=line.strip().split(':')[1].split('|')
        L=[int(_)for _ in line[0].split()]
        R=[int(_)for _ in line[1].split()]
        A.append([L,R])
S=len(A)
idx=1
for L, R in A:
    #print(L,R)
    w = 0
    for l in L:
        if l in R:
            w += 1
    r1 += int(2 ** (w-1))
    end = min(S, idx+w+1)
    for i in range(idx, end):#, w+bound):
        if not idx in D:
            D[idx] = [w, [i]]
        else:
            D[idx][1].append(i)
    d[idx]+=1
    for i in range(w):
        d[idx+1+i] += d[idx]
    idx+= 1
for _, v in d.items():r2+=v
print("part 1:", r1)
print("part 2:", r2)
