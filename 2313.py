F = 0 # 30677
from collections import defaultdict 
r1, r2 = 0, 0
A,B,sds=[],[],[]
D=[]
with open('13.' + str(F)) as file:
    t1,t2 = [],[]
    for line in file:
        line=line.strip()
        if not line:
            A.append(t1)
            B.append(t2)
            t1,t2=[],[]
        else:
            t1.append([_ for _ in line])
            t2.append(line)
    if t1: A.append(t1)
    if t2: B.append(t2)
for a in A: print(a)
for b in B: print(b)
idx = 0
for b in B:
    idx+=1
    H=False
    for i in range(1, len(b)):# - 1):
        if b[i] == b[i-1]:
            check = True
            u, d = i-1, i
            while u > -1 and d < len(b):
                if b[u] != b[d]:
                    check = False
                    break
                u -= 1
                d += 1
            if check:
                H=True
                r1 += i * 100
                break
    ### part 2 (HRZ)
    for i in range(1, len(b)):
        p2=0
        u, d = i-1, i
        while u > -1 and d < len(b):
            for uu,dd in zip([_ for _ in b[u]],[_ for _ in b[d]]):
                if uu != dd:
                    print('uu,dd',uu,dd,[_ for _ in b[u]],[_ for _ in b[d]])
                    p2+=1
            """
            if b[u] != b[d]:
                p2 += 1
            """
            u -= 1
            d += 1
        if p2 == 1:
            r2 += (i) * 100
            print('HRZ p2:', 'row', i, b[i-1],b[i])
            #break

    # print('hori' if H else ' - vert', r2)
    # if H:continue

    tp = list(list(_) for _ in zip(*b)) # transpose 
    # for line in tp: print(line)
    for i in range(1, len(tp)):# - 1):
        if tp[i] == tp[i-1]:
            check = True
            l, r = i-1, i
            while l > -1 and r < len(tp):
                if tp[l] != tp[r]:
                    check = False
                    break
                l -= 1
                r += 1
            if check:
                r1 += i
                break
    ### part 2 (VTC)
    for i in range(1, len(tp)):# - 1):
        p2=0
        l, r = i-1, i
        while l > -1 and r < len(tp):
            for ll,rr in zip(tp[l], tp[r]):
                if ll != rr:
                    print('ll,rr',ll,rr, tp[l],tp[r])
                    p2+=1
            """
            if tp[l] != tp[r]:
                p2 += 1
            """
            l -= 1
            r += 1 
        if p2 == 1:
            print('VTC p2:', 'col', i, tp[i-1],tp[i])
            r2 += i
            #break

print("part 1:", r1)
print("part 2:", r2)


