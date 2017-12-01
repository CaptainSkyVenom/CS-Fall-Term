import math
import random
def dist(x1, y1, x2, y2):
    return ((x2-x1)**2 + (y2-y1)**2)**(1/2)

def coinflip(num):
    if random.randint(0,num):
        return "Heads"
    return "Tails"


#x1,y1,x2,y2 =  map(int, input().split())

#print(dist(x1,y1,x2,y2))

print(coinflip())
