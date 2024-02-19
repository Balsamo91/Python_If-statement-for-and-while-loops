# print("""
      

# This is a package loading system program!
      

#       """)

# try:
#     user_input= int(input("How many items would you like to be shippped?: "))
# except ValueError:
#     print('Enter a valid number')
    

# items_number = user_input

# # Setting the maximum weight allowed per package
# max_weight_per_package = 20

# # Initialize all variables to zero
# total_weight = 0
# current_package_weight = 0 
# packages_sent = 0


# for i in range(items_number):
#     while True:
#                         # Here I decided to use a float() as the user may input a floating point number so this would catch it :) 
#         package_weight = float(input(f"What is the weight of the package(s)? (please state the weight between 1-10kg) {i + 1}:  "))

#             # Checking if the weight is within range 1 to 10 kg
#         if package_weight >= 1 and package_weight <= 10:
#             break  # Exit the loop if the weight is valid
#         else:
#             # Inform the user that the weight must be within the specified range
#             print("Weight must be between 1 and 10 kg. Please retry!")
        
#     # checking if adding the current weight would exceed the max weight per item
#     if package_weight + current_package_weight > max_weight_per_package:
#         packages_sent += 1  # Increment the package count as the current package has passed the 20kg limit and add +1 to package sent
#         print("""
              
# Maximum capacity has been achieved and the package has been marked as sent
              
#               """)
#         current_package_weight = package_weight # Starting a new package with the current item weight
#     else:
#         # If there is space in the current package for other items add them to package_weight
#         current_package_weight += package_weight

#     # Adding the current item weight to the total weight of all the packages
#     total_weight += package_weight

# # Adding the last package if it has any weight
# if current_package_weight > 0:
#     packages_sent += 1

# print(f"Number of package(s) sent: {packages_sent} \n\nTotal weight os package(s): {total_weight} \n\nTotal unused capacity: {packages_sent * max_weight_per_package - total_weight}\n")
   






###########################


while True:
    try:
       amount=int(input("how many do you want to buy "))
       break
    except ValueError:
       print("Please Enter An Amount")
       continue
    else:
        break