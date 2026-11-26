with open('9.txt') as r:
    sp = [[int(x) for x in line.split()] for line in r]
ans = 0
for a, b, c in sp:
    #pv = [x for x in line if line.count(x)==2]
    #np = [x for x in line if line.count(x)==1]
    #vse = [x for x in line]
    if a == 0 or b == 0 or c == 0 or a+b==0 or a+c==0 or b+c==0 or a+b+c==0:
        ans+=1
print(ans)