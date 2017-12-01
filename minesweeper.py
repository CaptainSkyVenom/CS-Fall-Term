import sys
import random

n = int(sys.argv[1])
m = int(sys.argv[2])
b = int(sys.argv[3])

grid = []
for i in range(n):
    row = [-1]*m
    grid.append(row)

for i in range(b):
    bombxpos = random.randint(0, n-1)
    bombypos = random.randint(0, m-1)
    while(grid[bombxpos][bombypos] != -1):
        bombxpos = random.randint(0, n-1)
        bombypos = random.randint(0, m-1)
    grid[bombxpos][bombypos] = 10

xvar = [1,1,-1,-1,0,0,1,-1]
yvar = [0,1,-1,0,1,-1,-1,1]

def inbounds(x, y):
    return x >= 0 and x < n and y >= 0 and y < m

for i in range(n):
    for j in range(m):
        if grid[i][j] == -1:
            grid[i][j] = 0
            for k in range(8):
                if inbounds(i + xvar[k], j + yvar[k]) and grid[i + xvar[k]][j + yvar[k]] == 10:
                    grid[i][j] += 1

for i in range(n):
    for j in range(m):
        if grid[i][j] == 10:
            grid[i][j] = '*'
        print(grid[i][j], end = ' ')
    print()
