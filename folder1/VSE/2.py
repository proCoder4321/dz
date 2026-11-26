print('y z x w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                if ((z==w)<=w)and(w<=(y and x)):
                    print(y, z, x, w)