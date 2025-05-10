# The code is a simple number guessing game where the user has to guess a number between 1 and 10.

import random # for challenge  

#target_number = 7
target_number = random.randint(1, 10) # for challenge

while True:
    
        number = int(input("Enter a number between 1 and 10 (inclusive): "))
        if 1 <= number <= 10:
            if number == target_number:
                print("Congratulations! You've guessed the correct number.")
                break
            elif number < target_number:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")
        else:
            print("Number is out of range. Please try again.")
