minn = float('inf')
def tr(numm):
    s=''
    while numm:
        s = str(numm%3)+s
        numm//=3
    return s
for n in range(1000):
    r = tr(n)
    r = r+str(n%3)
    r = int(r, 3)
    if len(str(r))==3:
        if r<minn:
            minn=r
print(minn)