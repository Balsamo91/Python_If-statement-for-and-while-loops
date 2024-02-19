import sys

print("""
      

This is a package loading system program!
      

      """)


# items_number = int(input("How many items would you like to be shippped?: "))

while True:
    try:
       items_number=int(input("How many items would you like to be shippped?: "))
       break
    except ValueError:
       print("Please Enter An Amount")
       continue
    else:
        break


# Setting the maximum weight allowed per package
max_weight_per_package = 20

# Initialize all variables to zero
total_weight = 0
current_package_weight = 0 
packages_sent = 0


while True:
    try:
        # Here I decided to use a float() as the user may input a floating point number so this would catch it :) 
        package_weight = float(input(f"What is the weight of the package(s)? (please state the weight between 1-10kg) {i + 1}:  "))       
        break
    except ValueError:
       print("\nPlease Enter the correct amount here for the WEIGH!\n")
       continue
    else:
        break

for i in range(items_number):
    while True:
        try:
              # Here I decided to use a float() as the user may input a floating point number so this would catch it :) 
            package_weight = float(input(f"What is the weight of the package(s)? (please state the weight between 1-10kg) {i + 1}:  "))
            
