# Ask user for their name
name = input("What's your name? ")

# Remove whitespace from str
name = name.strip()

# Capitalize user's name
name = name.capitalize()

# Say hello to user
# print("hello, ", end = "")
# print(name)
print(f"Hello, {name}")