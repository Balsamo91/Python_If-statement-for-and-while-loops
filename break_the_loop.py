print("Type 'exit' to stop the loop")

while True:
    response = input("> ")
    if response == "exit":
        break # Exit the loop
    print(f"You typed {response}")

print(f"Your {response} was successful!")