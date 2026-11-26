with open('9.txt') as r:
    sp = [[int(x) for x in line.split()] for line in r]
ans = 0
for line in sp:
    #pv = [x for x in line if line.count(x)==2]
    #np = [x for x in line if line.count(x)==1]
    vse = [x for x in line]
    a = max(vse)
    vse.remove(a)
    pr=1
    for x in vse:
        pr*=x
    if a**2>pr:
        ans+=1
print(ans)