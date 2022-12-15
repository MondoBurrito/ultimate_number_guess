# import curses  # Learn curses later...
import os
import re


os.system("clear")

print("u l 7 1 m 4 7 3   n u m b 3 r   6 u 3 5 5\n")


# Define the regex pattern that matches allowed characters.
pattern = r"^[a-zA-Z-'\s]+$"

# Use the regex pattern to check if the username is valid.
while True:
    username = input("Enter your name: ")

    if re.match(pattern, username):
        print(f"\nHello, {username}")
        break
    else:
        print(
            "That name is invalid. Please only use letters, spaces, "
            "hyphens, and apostrophes.\n"
        )
