F = 0
r1, r2 = 0, 0
A = []
def dbg(T):
    for t in T:print(' '.join(t))
    print()
with open('14.' + str(F)) as file:
    for line in file: A.append([_ for _ in line.strip()])
def TP(A):
    A = [ list(_) for _ in reversed(list(zip(*A)))]
    #dbg(A)
    nomove = [[] for _ in range(len(A))]
    for i,a in enumerate(A):
        if '#' not in a: continue
        for index, char in enumerate(a):
            if char == '#': nomove[i].append(index)
    for i, allpos in enumerate(nomove):
        #if pos: A[i] = sorted(A[i][:pos])[::-1] + A[i][pos:]
        if not allpos:
            A[i] = sorted(A[i])[::-1]
            #print('no cube')
            continue
        #print(allpos)
        prev = -1
        for pos in allpos:
            #print(A[i])
            A[i] = A[i][:prev+1] + sorted(A[i][prev+1:pos])[::-1] + A[i][pos:]
            #print(A[i])
            # if pos == 1: print(A[i][:prev+1], sorted(A[i][prev+1:pos])[::-1], A[i][pos:])
            prev = pos
        if prev != -1: A[i] = A[i][:prev+1] + sorted(A[i][prev+1:])[::-1]
        #print()
    return A
    #dbg(A)
### part 1
p2 = [list(_) for _ in A]
p1 = [list(_) for _ in A]
p1 = TP(p1)
for i, n in enumerate(list(zip(*p1))): r1 += n.count('O') * (len(p1) - i)

### part 2
cc=1000000000
#p2 = [list(_) for _ in A]
state=' '.join([' '.join(r)for r in p2])
#ALL = [state]
ALL=[p2]
S=set()
S.add(state)
seen = None
for i in range(cc)#1,cc+1):
    for _ in range(4):
        p2 = TP(p2)
        #dbg(p2)
    dbg(p2)
    # to set
    state  = ' '.join([' '.join(r)for r in p2])
    if state in S:
        seen = i+1
        break
    S.add(state)
    # to record
    ALL.append(p2)
print(seen)
print(ALL.index(p2))
idx = ALL.index(p2)
size = seen - idx
fact = (cc - seen) // size
idx = idx + fact%size 
for i, n in enumerate(list(zip(*ALL[idx]))): r2 += n.count('O') * (len(ALL[idx]) - i)

print("part 1:", r1)
print("part 2:", r2)
assert(r2 in [64,128,127])
# hi . 95082 101814

