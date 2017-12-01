binary = input()

num = 0
for i in range(len(binary)):
    num += 2**i * (ord(binary[len(binary)-1-i])-ord('0'))

print(num)
