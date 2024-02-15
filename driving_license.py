age = int(input("enter your age: "))
has_license = input("Do you have a driving license? (yes/no): ").lower()

if age >= 18:
    if has_license == "yes":
        print("you can drive!")
    else:
        print("you are old enough but you need a driver license")
else:
    print("you are not old enought to drive!!!!")