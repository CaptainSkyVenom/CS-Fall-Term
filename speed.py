speed = int(input())

CdateM = input("What is the current month? ")
CdateD = input("What is the current date? ")


BdateM = input("When is your birthday month? ")
BdateD = input("When is your birthday date? ")

wiggleroom = 0

if CdateM == BdateM and CdateD == BdateD:
    wiggleroom += 5

if speed <= 60 + wiggleroom:
    print("No ticket!")
else if(speed > 60 + wiggleroom and speed <= 80 + wiggleroom):
    print("Small ticket!")
else:
    print("Big ticket!")
