import sys
import numpy as np
def escaped(z1, z2, c1, c2, it):
    if it > 3:
        return 0
    if z1**2 + z2**2 >= 4:
        return it
    else:
        return escaped((z1**2 - z2**2) + c1, 2 * z1 * z2 + c2, c1, c2, it+1);

print(escaped(0,0, 1, 0, 0))


i = 2
j = -2
while i >= -2:
    while j <= 2:
        print(escaped(0,0, j, i , 0), end = ' ')
        j += 0.5
    print()
    j = -2
    i -= 0.5
