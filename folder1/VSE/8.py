import itertools as t
a = 'ЛЕВИОСА'
gl = 'ЕИОА'
sgl='ЛВС'
ans = 0
sp = [y for y in t.permutations(a)]
for x in sp:
    if x[0] not in gl and x[3] not in sgl:
        ans += 1
print(ans)