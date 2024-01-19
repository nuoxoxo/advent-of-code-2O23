infile=0 # 895 too hi 
Blocs = [] # a bloc is a tuple of tuple-pairs ((x,y,z),(x2,y2,z2))
with open('22.' + str(infile)) as file:
    for line in file:
        L, R = line.split('~')
        S = tuple([ int(_) for _ in L.split(',') ])
        E = tuple([ int(_) for _ in R.split(',') ])
        Blocs.append((S,E))
#for b in Blocs:print(b)
Beams = []
seen = set()
for bloc in Blocs:
    Beam = []
    s,e = bloc
    a, b, c = s
    aa,bb,cc = e    # vertical bloc
    if a == aa and b == bb:
        for _ in range(c, cc + 1):
            Beam.append( (a, b, _) )
    # X beam
    if b == bb and c == cc:
        for _ in range(a, aa + 1):
            Beam.append( (_, b, c) )
    # vertical bloc
    if c == cc and a == aa:
        for _ in range(b, bb + 1):
            Beam.append( (a, _, c) )
    for _ in Beam:
        seen.add( _ )
    Beams.append(Beam)

while True:
    moved = False
    for i, beam in enumerate(Beams) :
        stuck = False
        for (a, b, c) in beam:
            if c == 1: # on the ground
                stuck = True
            below = (a, b, c - 1) # possible if we check it bef. for loop
            if below not in beam and below in seen: # met another beam
                stuck = True
        if stuck:
            continue
        Beams[ i ] = [ (a, b, c - 1) for (a, b, c) in beam ]
        for (a, b, c) in beam:
            seen.discard( (a, b, c) )
            seen.add( (a, b, c - 1) )
        moved = True
    if not moved:
        break
print(seen, len(seen))

res = 0
for i, beam in enumerate(Beams) :
    for layer in beam:
        # suppose this one beam is not there
        seen.discard( layer )
    moved = False
    for k, other in enumerate(Beams):
        if k == i: continue
        stuck = False
        for layer in other:
            a, b, c = layer
            below = ( a, b, c - 1 )
            if below not in other and below in seen:#or c == 1:
                stuck = True
            if c == 1:
                stuck = True
        if not stuck:
            moved = True
    res += not moved
    for layer in beam:
        # end sim, added beam back
        seen.add( layer )
print(res)
assert(res in [ 405, 5 ])
