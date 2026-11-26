def pt(numm):
    s = ''
    while numm:
        s = str(numm % 5) + s
        numm //= 5
    return s
a = 5**20+5**10-5**13-5**3
b = pt(a)
print(sum([int(x) for x in b]))