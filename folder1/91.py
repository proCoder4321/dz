with open('9.txt') as r:
    sp = [[int(x) for x in line.split()] for line in r]
ans = 0
for line in sp:
    pv = [x for x in line if line.count(x)==2]
    np = [x for x in line if line.count(x)==1]
    if len (pv)==2 and len (np)==4:
        a = False
        for i in range(6):
            for j in range(i+1, 6):
                for k in range(j+1, 6):
                    summ = line[i]+line[j]+line[k]
                    if summ == sum(line)-summ:
                        a = True
        if a:
            ans += 1
print(ans)