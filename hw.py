import random
v = int(input())
t = int(input())

w = ""
while abs(t) > 50 or v > 120 or v < 3:
    print("OUT OF RANGE! TRY AGAIN")
    v = int(input())
    t = int(input())

w = 35.74 + 0.6215*t + (0.4275*t - 35.75) * v**0.16

print(w)

for i in range(1000, 2001):
    print(i, end = ' ')
    if i % 5 == 4:
        print()
print()
#prints one and zero in an alternating sequence until the length is 16.

inp = int(input())
count = 0
for i in range(inp):
    if random.randint(0,1):
        count += 1

print('% of heads: '+str(count/inp * 100) + '%')
