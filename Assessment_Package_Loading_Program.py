# for n in 
#     if items_number != float():
#        print("please enter only numbers!")
#     else:
#        continue

print("This is a package loading system program!")

items_number = int(input("How many items would you like to be shippped?: "))

max_weight_per_item = 20
total_weight = 0
current_package_weight = 0 # Keeping track of the current package's weight

for i in range(items_number):
    package_weight = float(input(f"What is the weight of the package(s)? (please state the weight of the item(s) one by one) {i + 1}:  "))
    print("codice pacco: " + str(i))

    # checking is adding the current weight would exceed the Max weight per item
    if package_weight + current_package_weight > max_weight_per_item:
        print("Codice pacco spedito: " + str(i))
        print(f"package_weight: {package_weight}")
        print(f"current_package_weight: {current_package_weight}")

        # package_sent = i
        # package_sent_weight = package_weight
        print("Maximum capacity has been achieved and the package(s) have been marked as sent")
        # current_package_weight = 0 # Resetting the package weight for next item
    
# Adding the current item weight to current package
    # current_package_weight += package_weight
    # total_weight += package_weight

    # if total_weight <= 0:
    #     print("Error: Values less or equal to 0 is not accepted! Please retry.")
    #     break

# print(f"Number of package(s) sent: {items_number} \nTotal weight os package(s): {total_weight} \nTotal unused capacity: {items_number * max_weight_per_item - total_weight}")
   
# print(current_package_weight)

# print(f"{package_sent} + {package_sent_weight}")






#        if total_weight 
# while True:



# print("total weight:", total_weight)





# ###########

# job_count = int(input("Enter the number of items: "))

# workload1 = 0
# workload2 = 0
# workload3 = 0

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
