import random

again = 'y'

while again == 'y':
    number = random.randrange(1,101)

    answer = int(input("Guess The Number: "))

    while answer != number:
        print("Wrong number!")
        if answer < number:
            print("Too Low!")
        else:
            print("Too High!")
        answer = int(input("Guess Again: "))

    print("You win!")
    again = input("Would you like to play again? y/n: ")
