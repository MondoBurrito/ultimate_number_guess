import os
import random
import re  # regex
import time


def main_menu(name):
    """
    This module is the main menu.

    Args:
        name (str): User's initials.
    Returns:
        XXXXXXXX fill in later XXXXXXXXXXXXXXXX.
    """

    print(typewriter("...", 1.0))

    welcome_msg = f"> User {name} successfully logged in.\n"

    print(typewriter(welcome_msg, 0.05))


def check_name():
    """
    This module accepts the user's name and checks it for invalid characters
    using a regex pattern.

    Returns:
        Returns the user's name once it has been verified.
    """
    initials_pattern = r"^[a-zA-Z\s\d]{2,3}$"  # Two to three alphanumeric, spaces.

    while True:

        name_input = input(typewriter("> Enter your initials: ", 0.05)).upper()

        if re.match(initials_pattern, name_input):
            return name_input
        else:
            print("Invalid initials.")


def random_number(name):
    """
    This module sets the difficulty and runs the number guessing conditional
    statements.

    Args:
        name (str): User's initials.
    Returns:
        XXXXXXXX fill in later XXXXXXXXXXXXXXXX.
    """
    random_num = random.randint(1, 100)
    guess_count = 1

    while guess_count <= 10:
        guess = int(input(f"Guess {guess_count}: "))

        if guess > random_num:
            print("Too large.\n")
            guess_count += 1
        elif guess < random_num:
            print("Too small.\n")
            guess_count += 1
        elif guess == random_num:
            print(
                typewriter(
                    f"> Well done, {name}! You guessed the number "
                    f"{guess} in {guess_count} tries.",
                    0.05,
                )
            )
            break
    return


def typewriter(text, delay):
    """
    This module creates a typewrite effect for print statements.

    Args:
        text (str): Text to be printed.
    Returns:
        Returns empty string to avoid returning None.
    """
    output = ""
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    return output


# =============================================================================


os.system("clear")

print("u l 7 1 m 4 7 3   n u m b 3 r   6 u 3 5 5\n")

name = check_name()

main_menu(name)

print(typewriter("> Guess a number between 1 and 100\n", 0.05))

random_number(name)


print("\nG A M E   O V E R")
