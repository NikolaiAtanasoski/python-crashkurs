#2.3
name = "phil"
print(f"Hello {name.title()}, would you like to learn some Python today?")

#2.4
first_name = "pHiL"
last_name = "LiMbEcK"
print("original: \n\t{} {}".format(first_name,last_name))
print(f"lowercase: \n\t{first_name.lower()} {last_name.lower()}")
print(f"uppercase: \n\t{first_name.upper()} {last_name.upper()}")
full_name = f"{first_name.lower()} {last_name.lower()}"
print(f"title: \n\t{full_name.title()}")

#2.5
print('Albert Einstein once said, "A person who never made a mistake never tried anything new."')

#2.6
famous_person="albert einstein"
message = f'{famous_person.title()} once said, "A person who never made a mistake never tried anything new."'
print(message)

#2.7
name = "\n  \t asdadasd  \n  \t"
print(f"original: {name}")
print(f"lstrip: {name.lstrip()}")
print(f"rstrip: {name.rstrip()}")
print(f"strip : {name.strip()}")


