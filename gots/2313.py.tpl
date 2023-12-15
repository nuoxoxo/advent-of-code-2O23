F = 0
r1, r2 = 0, 0
A = []
def dbg(T):
    for t in T:print(t)
with open('13.' + str(F)) as file:
    temp = []
    for line in file:
        line=line.strip()
        if not line:
            A.append(temp)
            temp = []
        else:
            temp.append([_ for _ in line])
    if temp:
        A.append(temp)
# dbg(A)
for line in A:
    H=False
    for i in range(1, len(line)):
        if line[i] == line[i - 1]:
            check = True
            u, d = i - 1, i
            while u > -1 and d < len(line):
                if line[u] != line[d]:
                    check = False
                    break
                u -= 1
                d += 1
            if check:
                H=True
                r1 += i * 100
                break

    ### part 2 (HRZ)

    for i in range(1, len(line)):
        p2 = 0
        u, d = i - 1, i
        while u > -1 and d < len(line):
            for U, D in zip(line[u], line[d]):
                if U != D:
                    p2+=1
            u -= 1
            d += 1
        if p2 == 1:
            r2 += (i) * 100
            print('HRZ p2:', 'row', i, '\n',''.join(line[i-1]),'\n',''.join(line[i]),'\n')
            break
    tp = list(list(_) for _ in zip(*line)) # transpose
    for i in range(1, len(tp)):
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

    # print('hori' if H else ' - vert',)
    # if H:continue # part 1 can break p2 cannot

    ### part 2 (VTC)

    for i in range(1, len(tp)):
        p2 = 0
        l, r = i - 1, i
        while l > -1 and r < len(tp):
            for L, R in zip(tp[l], tp[r]):
                if L != R:
                    p2+=1
            l -= 1
            r += 1 
        if p2 == 1:
            print('VTC p2:', 'col', i, '\n',''.join(tp[i - 1]),'\n',''.join(tp[i]),'\n')
            r2 += i
            break

print("part 1:", r1)
print("part 2:", r2)



