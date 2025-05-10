# The code is a simple number guessing game where the user has to guess a number between 1 and 10.

import random # for challenge  

#target_number = 7
target_number = random.randint(1, 10) # for challenge

guesses = []

while True:
    
        number = int(input("Enter a number between 1 and 10 (inclusive): "))
        if 1 <= number <= 10:
            guesses.append(number)
            if number == target_number:
                print(f"Congratulations! {target_number} is the correct number.")
                break
            elif number < target_number:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")
        else:
            print("Number is out of range. Please try again.")

# lowest = min(guesses)
# highest = max(guesses)

lowest = guesses[0]
highest = guesses[0]
for guess in guesses:
     if guess > highest:
          highest = guess
    
     if guess < lowest:
          lowest = guess

msg = "Your highest guess was {}, and your lowest guess was {}".format(highest, lowest)
print(msg)

# challenge - allows for negative values
high_dev = highest - target_number  
low_dev = target_number - lowest
print(f"Your highest guess was {high_dev} from the target.\nYour lowest guess was {low_dev} from the target.")
