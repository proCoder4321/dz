with open('9.txt') as r:
    sp = [[int(x) for x in line.split()] for line in r]
ans = 0
for line in sp:
    pv = [x for x in line if line.count(x)==2]
    np = [x for x in line if line.count(x)==1]
    vse = [x for x in line]
    if len(pv)==2 and len(np)==2:
        a = max(vse)
        vse.remove(a)
        if a< sum(vse):
            ans += 1
print(ans)