def sumofdigits(num):
    if num < 10:
        return num
    a = num%10
    num //= 10
    return sumofdigits(num) + a

def adjchars(str, i = 0):
    if i == len(str)-1:
        return str
    if str[i] == str[i+1]:
        newstr = ''
        for j in range(i):
            newstr += str[j]
        for j in range(i+1,len(str)):
            newstr += str[j]

        return adjchars(newstr, i)

    return adjchars(str, i+1)

def factorial(n):
    if n < 0:
        return -1
    if n == 0:
        return 1
    if n == 1:
        return n
    return n * factorial(n-1)
#
# print(sumofdigits(int(input("Enter number to find sum of digits: "))))
# print(adjchars(input("Enter string to be cleaned: ")))
print(factorial())
