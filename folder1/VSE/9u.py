with open('9.txt') as r:
    sp = [[int(x) for x in line.split()] for line in r]
ans = 0
n = 0
for line in sp:
    n+=1
    a = False
    b = False
    if int(line[0])<int(line[1]) and int(line[1])<int(line[2]) and int(line[2])<int(line[3]) and int(line[3])<int(line[4]):
         a = True
    if len(line)!=len(set(line)):
        b = True
    if a or b:
        ans+=n
print(ans)