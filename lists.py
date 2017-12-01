import random
l = []
l2 = [1,2,3]
l2.append(4)
l2.pop(0)
l2.pop()
l2.remove(2)
print(l2[-1])


l3 = [1,2,3,4,5,6]
l3[2] = 0
print(len(l3))
l3[2], l3[1] = l3[1], l3[2]
print(l3)

l4 = []
for i in range(100):
    l4.append((i+1)*7)

print(l4)

print(l4[random.randint(0,100)])

lis = []

def order(lis):
    newlis = []
    for i in lis:
        smallest = min(lis)
        lis.remove(smallest)
        newlis.append(smallest)

    return newlis


#generate 10 random values between 0 and 100, and for the values in the even positions, they should be in decreasing order.
#for the values in the odd positions, they should be in increasing order.

for i in range(10):
    lis.append(random.randint(0,100))

leftlist = []
declist = []
for i in range(10):
    if i % 2 == 0:
        declist.append(lis[i])
    else:
        leftlist.append(lis[i])

leftlist.sort()
declist.sort()
declist.reverse()

print(declist)
print(leftlist)

newlis = []
for i in range(5):
    newlis.append(declist[i])
    newlis.append(leftlist[i])

print(newlis)
