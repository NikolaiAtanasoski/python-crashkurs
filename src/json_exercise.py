from pathlib import Path
import json

target_dir = "./target"
filename = "usernames.json"
full_path = f"{target_dir}/{filename}"


class User:

    def __init__(self, username, favorite_number):
        self.username = username
        self.favorite_number = favorite_number


def load_users():
    try:
        with open(full_path, 'r') as users_file:
            users = json.load(users_file)
            return users
    except FileNotFoundError:
        return []


def save_users(users):
    Path(target_dir).mkdir(parents=True, exist_ok=True)
    with open(full_path, 'w') as file:
        json.dump(users, file)


def greet_user():
    registered_users = load_users()
    current_username = input("Welcome! who are you?\n> ")
    if current_username in registered_users:
        print("amk")
        # current_user = registered_users.getByName??
        # print(f"Welcome back {current_user.username}! Your favorite Number is: {current_user.favorite_number}")
    else:
        favorite_number = input("And what is your favorite number?\n>")
        new_user = User(current_username, int(favorite_number))
        registered_users.append(new_user)
        save_users(registered_users)
        print("bye!")

u1 = User("amk",15)
print(u1.__dict__)
# greet_user()

