with open('9.txt') as r:
    sp = [[int(x) for x in line.split()] for line in r]
ans = 0
for line in sp:
    pv = [x for x in line if line.count(x)==2]
    np = [x for x in line if line.count(x)==1]
    if len(pv)==4 and len(np)==2:
        if sum(pv)>sum(np):
            ans+=1
print(ans)