filename = "pi_million_digits.txt"

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ""
for line in lines:
    pi_string += line.strip()

is_running = True
while is_running:
    print()
    birthday = input("Enter your birthday and I will check if it is appaers within the first\nmillion digits of pi: ")
    if birthday in ["q", "quit", "exit", "bye"]:
        is_running = False
        print("bye!")
        exit(0)
    elif birthday in pi_string:
        print("Your birthday appears in the first million digits of pi!")
        print(f"Starting at: {pi_string.index(birthday)}")
    else:
        print("Too bad, your birthday does not appear in the first million digits of pi.")
