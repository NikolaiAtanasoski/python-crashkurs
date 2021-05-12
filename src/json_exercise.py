from pathlib import Path
import json

target_dir = "./target"
filename = "usernames.json"
full_path = f"{target_dir}/{filename}"
Path(target_dir).mkdir(parents=True, exist_ok=True)

with open(full_path, 'w') as file:
    username = input("Enter username: ")
    json.dump(username, file)
    print(f"We will remember you, {username}")

with open(full_path, 'r') as file:
    username = json.load(file)
    print(f"Welcome back, {username}")
