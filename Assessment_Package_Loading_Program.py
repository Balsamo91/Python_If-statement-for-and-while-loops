
print("This is a package loading system program!")

items_number = int(input("How many items would you like to be shippped?: "))

# for n in 
#     if items_number != float():
#        print("please enter only numbers!")
#     else:
#        continue

total_weight = 0

for i in range(items_number):
    package_weight = float(input(f"What is the weight of the package? (please state the weight of the item(s) one by one) {i + 1}:  "))
    total_weight += package_weight
if total_weight <= 0:
    print("Error: Values less or equal to 0 is not accepted! Please retry.")
    # if total_weight 
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
