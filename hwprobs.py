##hw 4

lis = []
for i in range(100):
    lis.append(i)

leftlist = []
declist = []
for i in range(100):
    if i % 2 == 0:
        declist.append(lis[i])
    else:
        leftlist.append(lis[i])

leftlist.sort()
declist.sort()
declist.reverse()

newlis = []
for i in range(50):
    newlis.append(declist[i])
    newlis.append(leftlist[i])

print(newlis)


##hw 1
prime = []
for i in range(1001):
    prime.append(1)

for p in range(2, 35):
    if prime[p] == 1:
        for i in range(p*2, 1001, p):
            prime[i] = 0

prime[0] = 0
prime[1] = 0

print("\n\n\n\nprimes: ")
for i in range(len(prime)):
    if prime[i]:
        print(i, end = ' ' )
