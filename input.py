import sys

year = int(input())

result = not bool(year%4)
result2 = not bool(year%100)
result3 = not bool(year%400)

result4 = not (result2 and not result3)
result5 = result4 and result

print(result5)

n = int(input())
sum = n * (n+1) / 2
print(sum)
