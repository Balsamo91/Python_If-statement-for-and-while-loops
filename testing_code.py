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



def main():
    num_items = int(input("Enter the number of items: "))
    total_weight = 0
    
    for i in range(num_items):
        item_weight = float(input(f"Enter the weight of item {i + 1}: "))
        total_weight += item_weight
    
    print("Total weight:", total_weight)

if __name__ == "__main__":
    main()