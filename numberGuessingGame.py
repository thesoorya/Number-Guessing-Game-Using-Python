import random

highest_number = input("Enter the number : ")

if highest_number.isdigit():
    highest_number = int(highest_number)

    if highest_number < 0 :
        print("Please enter larger than 0")

else:
    print("please enter valid number")
    quit()

random_number = random.randint(0,highest_number)

while True:
    user_guess = input("Make the guess : ")

    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("please enter valid number")
        continue

    if user_guess == random_number:
        print("You got it!")
        break
    else:
        print("You got it wrong")