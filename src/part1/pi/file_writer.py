from pathlib import Path

target_dir = "./target"
filename = "some_output.txt"
full_path = f"{target_dir}/{filename}"
Path(target_dir).mkdir(parents=True, exist_ok=True)

with open(full_path, 'w') as file:
    file.write("way\n")
    file.write("amk")

with open(full_path, 'r') as file:
    print(file.read())

