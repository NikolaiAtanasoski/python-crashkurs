filename = "some_output.txt"

with open(filename, 'w') as file:
    file.write("way\n")
    file.write("amk")

with open(filename, 'r') as file:
    print(file.read())

