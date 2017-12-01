grade = int(input())

grades = ['A', 'B', 'C', 'D', 'F']
check = 89
for i in range(10):
    if grade > check:
        print(grades[min(4,i)])
        break
    check -= 10
