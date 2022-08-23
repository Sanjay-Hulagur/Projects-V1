print("Python is configured2")

import random

top_of_range = input("Please type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("type a number larger than 0")
        quit()
else:
     print("Please type a number next time.")
     quit()

random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Guess the random Number: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time.")
        quit()
    if user_guess > random_number:
        print("you guesed higher")
    elif user_guess < random_number:
        print("you guessed lower.")

    if user_guess == random_number:
        print("Noice - you got it correct")
        break
    else:
        print("Keep trying my friend, your answer was wrong")
        continue

print("you took " + str(guesses) + " Guesses to ge the correct number")
