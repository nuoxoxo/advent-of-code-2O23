F = 0
r1, r2 = 0, 0
A = []
def dbg(T):
    for t in T:print(' '.join(t))
    print()
with open('14.' + str(F)) as file:
    for line in file:
        A.append([_ for _ in line.strip()])
A = [ list(_) for _ in reversed(list(zip(*A)))]
dbg(A)
nomove = [[] for _ in range(len(A))]

for i,a in enumerate(A):
    if '#' not in a:
        continue
    for index, char in enumerate(a):
        if char == '#':
            nomove[i].append(index)

for i, allpos in enumerate(nomove):
    #if pos: A[i] = sorted(A[i][:pos])[::-1] + A[i][pos:]
    if not allpos:
        A[i] = sorted(A[i])[::-1]
        print('no cube')
        continue
    print(allpos)
    prev = -1
    for pos in allpos:
        #print(A[i])
        A[i] = A[i][:prev+1] + sorted(A[i][prev+1:pos])[::-1] + A[i][pos:]
        #print(A[i])
        # if pos == 1: print(A[i][:prev+1], sorted(A[i][prev+1:pos])[::-1], A[i][pos:])
        prev = pos
    if prev != -1:
        A[i] = A[i][:prev+1] + sorted(A[i][prev+1:])[::-1]
    print()

dbg(A)
for i, n in enumerate(list(zip(*A))): r1 += n.count('O') * (len(A) - i)

cc=1000000000

print("part 1:", r1)
print("part 2:", r2)

