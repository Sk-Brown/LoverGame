# Importing colors module
from random import randint
from colors import *

# Welcome Screen
print( YELLOW, "Welcome to Lover Game")
user_input = int(input(WHITE + "1. Start Game\n"
                               "2. About Game\n"
                               "3. Exit Application\n\n"
                               "Choose An Option Above: "))

# Determine user input
if user_input == 1:
    user_input = int(input(WHITE + "Choose Game Level\n"
                  "1. Lazy (1-100)\n"
                  "2. Intermediate (1-500)\n"
                  "3. Hard (1-1000)\\n"
                  "Provide Level: "))
    # Determine the guess range
    guess_range = 0
    if user_input == 1:
        guess_range = 100
    elif user_input == 2:
        guess_range = 500
    elif user_input == 3:
        guess_range = 1000

#         Generate random number based on the guess range
    generated_number = randint(1, guess_range)
#     User guessing attempts
    user_chances = 3
    for chance in range(3):
        user_guess = int(input(WHITE + "Provide Your Guess Number: "))

#         Determine / Validate user guess
        if user_guess == generated_number:
            print(GREEN, f"Congrats Uer, You Guessed {generated_number} Right")
            break
        elif user_guess > generated_number:
            print(YELLOW, f"{user_guess} Is too High, Guess Again")
            user_chances = user_chances - 1
            break
        elif user_guess < generated_number:
            print(ROSY_PINK, f"{user_guess} Is Too Low, Guess Again")
            user_chances -= 1
    if user_chances < 1:
        print(RED, f"You Failed, Try Again\n"
                   f"The Correct Guess Number is {generated_number}")

elif user_input == 2:
    print(YELLOW, "This game is about Guessing the correct number!!!")
elif user_input == 3:
    print(WHITE, "Hope to see you again Gamer!")
    # Helper method to close program
    exit(101)
else:
    print(RED, "Invalid option. Try again!!!")
