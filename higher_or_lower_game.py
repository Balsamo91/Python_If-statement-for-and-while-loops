###

###


# Pseudocode (is a way to breakdown the task in a step by step way to visualize the task)

# 1. Generate a random number using 'random' module
import random

target_number = random.randint(1, 100)

# 2. Variable guessed_correctly set to false
guessed_correctly = False

# 3. Start our while loop and as user the number
while not guessed_correctly:
    user_input = input("Guess a number between 1 and 100: ")


    if user_input.isdigit():
        user_input = int(user_input)
    else:
        print("Please provide an Integer")
        continue
        

# 4. inside while loop check if the number is higher, lower or equal
    if user_input < target_number:
        print("Higher!")
    elif user_input > target_number:
        print("lower!")
    else:
        print("Amazing, you have found the number!")
        guessed_correctly = True
        print("It's the end of the loop!")

# 5.
# 6.
# 7.

