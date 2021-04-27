
print("Welcome, tell me your age to see how much it costs to see a movie, enter 'quit' to exit")

prompt = "\nage:"
active = True

while active:
    print(prompt)
    _input = input("> ")
    if _input == "quit":
        active = False
    else:
        price = 15
        age = int(_input)
        if age < 3:
            price = 0
        elif age <= 12:
            price = 10
        print(f"Your ticket costs {price}€.")
