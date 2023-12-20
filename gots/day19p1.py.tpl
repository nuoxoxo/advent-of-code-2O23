F = 0
r1, r2 = 0, 0
A = []
from collections import defaultdict
def DBG_( Dict ):
    for k,v in Dict.items(): print(k,v)
    print()
def Printer(*args):
    for arg in args: print(arg, end=' ')
    print()

D = defaultdict(list)
flow, todo, up, down = [],[],None,None

with open('19.' + str(F)) as file:
    up, down = [_.split('\n') for _ in file.read().strip().split('\n\n')]

#up = ['ex{x>10:one,m<20:two,a>30:R,A}']
for line in up:
    name, rules = line.split('{')
    rules = rules.split(',')
    end, rules = rules[-1][:-1], rules[:-1]
    # Printer('got:',name,end,'rules:',len(rules),rules)
    for rule in rules:
        cond, dest = rule.split(':')
        key, op, val = cond[0],cond[1],int(cond[2:])
        # Printer("rule:",key,op,val,dest)
        D[name].append([ key, op, val, dest ])
    D[name].append(end)

#DBG_( D )

for line in down:
    flow = defaultdict(int)
    line = line[1:-1].split(',')
    for xpr in line:
        key, val = xpr.split('=')
        flow[key] = int(val)
    #DBG_(flow)
    res = None
    curr = 'in'
    found = False
    while not found:
        for line in D[curr]:
            good = False
            if isinstance(line, str):
                if line in 'AR':
                    res = line
                    found = True
                    break
                curr = line
            else:
                key, op, val, dest = line
                # Printer('line?',key, op, val, dest)
                if op == '>':
                    good = flow[key] > val
                elif op == '<':
                    good = flow[key] < val
                else:
                    die('wtf')
            if good:
                if dest in 'AR':
                    res = dest
                    found = True
                    break
                curr = dest
                break
            
    if found and res == 'A':
        #print('WIN')
        #DBG_(flow)
        r1 += sum(flow.values())

print("part 1:", r1)
print("part 2:", r2)


