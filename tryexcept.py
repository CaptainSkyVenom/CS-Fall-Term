def subtract(a,b):
    try:
        return a - b
    except TypeError:
        print('Wrong data type')
        return None

def check(a,b):
    try:
        a = int(a)
        b = int(b)
        return 0
    except ValueError:
        print("Wrong Data Type")
        return 1

a = input()
b = input()

while(check(a,b)):
    a = input()
    b = input()

a = int(a)
b = int(b)

print(subtract(a,b))
