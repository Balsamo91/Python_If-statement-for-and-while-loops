# # job_count = int(input("Enter the number of items: "))

# workload1 = 0
# workload2 = 0
# workload3 = 0
# # for job in range(job_count):
# #     print("Enter the number of working hours for the car")
# #     job_hours = int(input ())
# #     if job_hours <= 0:
# #         print("Error: Invalid number of hours!")
# #         break
# #     if workload3 < workload1 and workload3 < workload2:
# #         workload3 += job_hours
# #     elif workload2 < workload1:
# #         workload2 += job_hours
# #     else:
# #         workload1 += job_hours
# # print("The nearest mechanic will be free within {} days".format(
# #     int((min(workload1, workload2, workload3) + 7) / 8)
# # ))
# # print("All mechanics will be free within {} days ".format(
# #     int((max(workload1, workload2, workload3) +7) / 8)
# # ))


# job_count = int(input("Enter the number of items: "))

# for job in range(job_count):
#     print("Enter the number of working hours for the job")
#     job_hours = int(input())
#     if job_hours <= 0:
#         print("Error: Invalid number of hours!")
#         break
#     if workload3 < workload1 and workload3 < workload2:
#         workload3 += job_hours
#     elif workload2 < workload1:
#         workload2 += job_hours
#     else:
#         workload1 += job_hours
# print("The nearest mechanic will be free within {} days".format(
#     int((min(workload1, workload2, workload3) +7) / 8)
# ))
# print("All mechanics will be free within {} days ".format(
#     int((max(workload1, workload2, workload3) +7) / 8)
# ))



# def main():
#     num_items = int(input("Enter the number of items: "))
#     total_weight = 0
    
#     for i in range(num_items):
#         item_weight = float(input(f"Enter the weight of item {i + 1}: "))
#         total_weight += item_weight
    
#     print("Total weight:", total_weight)

# if __name__ == "__main__":
#     main()

import sys



print("""
      

This is a package loading system program!
      

      """)




try:
    items_number = int(input("How many items would you like to be shippped?: "))
except ValueError:
    print("This is not a number")

# for n in range(items_number):
#     if n != items_number:
#         sys.exit()
#     else:
#         continue
# # 
# try:
#     if not items_number.is_integer():
#         exit()
# except ValueError:
#     print('Enter a valid number')
    

# Setting the maximum weight allowed per package
max_weight_per_package = 20

# Initialize all variables to zero
total_weight = 0
current_package_weight = 0 
packages_sent = 0


for i in range(items_number):
    while True:
                        # Here I decided to use a float() as the user may input a floating point number so this would catch it :) 
        package_weight = float(input(f"What is the weight of the package(s)? (please state the weight between 1-10kg) {i + 1}:  "))

            # Checking if the weight is within range 1 to 10 kg
        if package_weight >= 1 and package_weight <= 10:
            break  # Exit the loop if the weight is valid

            # If weight input is less or equal to zero, program interrupts.
        elif package_weight <= 0:
            print("Item weight cannot be less or equal to 0")
            sys.exit()

        else:
            # Inform the user that the weight must be within the specified range
            print("Weight must be between 1 and 10 kg. Please retry!")
            
            
        
    # checking if adding the current weight would exceed the max weight per item
    if package_weight + current_package_weight > max_weight_per_package:
        packages_sent += 1  # Increment the package count as the current package has passed the 20kg limit and add +1 to package sent
        print("""
              
Maximum capacity has been achieved and the package has been marked as sent
              
              """)
        # Starting a new package with the current item weight
        current_package_weight = package_weight 
    else:
        # If there is space in the current package for other items add them to package_weight
        current_package_weight += package_weight

    # Adding the current item weight to the total weight of all the packages
    total_weight += package_weight

# Adding the last package if it has any weight
if current_package_weight > 0:
    packages_sent += 1

print(f"\nNumber of package(s) sent: {packages_sent} \n\nTotal weight os package(s): {total_weight} \n\nTotal unused capacity: {packages_sent * max_weight_per_package - total_weight}\n")
   

