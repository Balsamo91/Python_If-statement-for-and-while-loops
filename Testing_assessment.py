print("This is a package loading system program!")

items_number = int(input("How many items would you like to be shippped?: "))

max_weight_per_item = 20
total_weight = 0
current_package_weight = 0 # Keeping track of the current package's weight

for i in range(items_number):
    package_weight = float(input(f"What is the weight of the package(s)? (please state the weight of the item(s) one by one) {i + 1}:  "))
    print("codice pacco: " + str(i))
    # used_riporto = riporto + package_weight
    
    

    # checking is adding the current weight would exceed the Max weight per item
    if package_weight + current_package_weight > max_weight_per_item:
        riporto = package_weight - max_weight_per_item
        print("Codice pacco spedito: " + str(i))
        print(f"package_weight: {package_weight}")
        print(f"current_package_weight: {current_package_weight}")
        print(f"riport pacco: {riporto}")
        print("Maximum capacity has been achieved and the package(s) have been marked as sent")

        if riporto >= 1:
            used_riporto = riporto + package_weight
            print(f"used riport: {used_riporto}")

    
# Adding the current item weight to current package
    total_weight += package_weight

    if total_weight <= 0:
        print("Error: Values less or equal to 0 is not accepted! Please retry.")
        break

# print(f"Number of package(s) sent: {items_number} \nTotal weight os package(s): {total_weight} \nTotal unused capacity: {items_number * max_weight_per_item - total_weight}")
   