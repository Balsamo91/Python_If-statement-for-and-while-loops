# age = int(input("enter your age: "))

# # check  if user is eligible to vote
# if age >= 18:
#     print("You are eligible to vote.")
# elif age < 0:
#     print("Error: Age cannot be negative!!!")
# else:
#     print("you are not eligible to vote yet.")



################
    
# age = int(input("enter your age: "))

# # check  if user is eligible to vote
# if age >= 18 and age <= 75: 
#     print("You are eligible to vote.")
# elif age < 0:
#     print("Error: Age cannot be negative!!!")
# else:
#     print("you are not eligible to vote yet.")


################
    
# age = int(input("enter your age: "))

# # check  if user is eligible to vote
# if age >= 18 and age <= 75:
#     print("You are eligible to vote.")
# elif age < 0 or age > 120:
#     print("Error: Age cannot be negative!!! (or your are probably dead!!)")
# elif age == 0:
#     print("you are not born yet!")
# else:
#     print("you are not eligible to vote yet.")

################

age = float(input("enter your age: "))
print(age)
# check  if user is eligible to vote
if age >= 18 and age <= 75:
    print("You are eligible to vote.")
elif age < 0 or age > 120:
    print("Error: Age cannot be negative!!! (or your are probably dead!!)")
elif age == 0:
    print("you are not born yet!")
else:
    print("you are not eligible to vote yet.")
