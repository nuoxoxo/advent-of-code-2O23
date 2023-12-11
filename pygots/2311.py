F = 0
r1, r2 = 0, 0
A = []
nul,gal='.','#'
with open('11.' + str(F)) as file:
    for line in file:
        line=line.strip()
        A.append(line)
G = []
for r, row in enumerate(A):
    for c, node in enumerate(row):
        if node != nul :
            assert(node is gal)
            G.append((r, c))
R,C=len(A),len(A[0])
ER,EC = [], [] # empty rs and cs
IA = [ [A[r][c] for r in range(R)] for c in range(C) ]
for i, r in enumerate(A):
    if any(node != nul for node in r):
        continue
    ER.append(i)
for i, c in enumerate(IA):
    if any(node != nul for node in c):
        continue
    EC.append(i)

def calc(G,xp=2) -> int:
    res = 0
    for i, node in enumerate(G):
        r, c = node
        for node_next in G[:i]:
            next_r, next_c = node_next
            s,e = min(next_r,r), max(r,next_r)
            for node in range(s, e):
                if node in ER:
                    res += xp
                    continue
                res += 1
            s,e = min(next_c, c), max(c, next_c)
            for node in range(s, e):
                if node in EC:
                    res += xp
                    continue
                res += 1
        #yield res
    return res

r2 = calc(G,int(1e6))
print('part 1:', calc(G))
print('part 2:', r2)
# 8871874186836 . 25930568

