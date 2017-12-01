import random

a = random.random()
print(a)

if a < 0.5:
    print("Tails")
else:
    print("Heads")

arr = []
for i in range(5):
    arr.append(random.randrange(0, 101))
    print(arr[i])

print(sum(arr)/5)
print(min(arr))
print(max(arr))
