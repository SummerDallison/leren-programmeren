amount = 0

while True:
    user_input = input("? ")
    amount += 1

    if user_input.lower() == "quit":
        break

print(f"Het aantal iteraties: {amount}.")