# Built-in libraries
import csv
import curses
import os
import random
import re
import time

# 3rd-party libraries
import getch


def check_name():
    """
    Accept the user's name and checks it for invalid characters using a regex
    pattern.

    Returns:
        Returns the user's name once it has been verified.
    """
    initials_pattern = r"^[a-zA-Z\s\d]{2,3}$"  # Two to three alphanumeric, spaces.

    while True:

        name_input = input(typewriter("> Enter your initials: ")).upper()

        if re.match(initials_pattern, name_input):
            print(typewriter(f"> User {name_input} successfully logged in."))
            return name_input
        else:
            print("Invalid initials.")


def main_menu(name):
    """
    Displays options for the user to choose.

    Args:
        name (str): User's initials.
    """

    print("\nMAIN MENU:")
    print(typewriter(f"  > Choose an option. "))

    print("\n  [1] Play game")
    print("  [2] Leaderboard")
    print("  [3] Quit\n")

    # Accept input without the user pressing <enter>.
    while True:
        key = getch.getch()
        if key == "1":
            game_code(name)
        if key == "2":
            get_leaderboard()
        if key == "3":
            exit()
        else:
            continue


def game_code(name):
    """
    Set the difficulty and run the number guessing conditional statements.

    Args:
        name (str): User's initials.
    Returns:
        guess_count (int): The number of guesses the user took to win.
    """
    difficulty = int(
        input("> Set your difficulty level. (1 - Easy, 2 - Med, 3 - Hard)\n")
    )

    if difficulty == 1:
        high_limit = 10
    elif difficulty == 2:
        high_limit = 100
    elif difficulty == 3:
        high_limit = 1000

    random_num = random.randint(1, high_limit)
    guess_count = 1

    print(typewriter(f"> Guess a number between 1 and {high_limit}\n"))

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
                    f"{guess} in {guess_count} tries.\n"
                )
            )
            # Add score to CSV file for storage.
            update_leaderboard(name, guess_count)
            main_menu(name)

        else:
            print("Invalid input.")

    print("YOU LOSE! ")

    return guess_count


def update_leaderboard(name, guess_count):
    """
    Add the user's score to a leaderboard CSV file.

    Args:
        name (str): User's initials.
        guess_count (int): The number of guesses the use took to win.
    """
    # Open CSV file in write mode.
    with open("leaderboard.csv", "a", newline="") as leaderboard:
        # Create the CSV writer.
        writer = csv.writer(leaderboard)
        # Write a row to the CSV file.
        writer.writerow([name, guess_count])


def get_leaderboard():
    """
    Retrieve the leaderboard data and sort it

    Args:
        name (str): User's initials.
        guess_count (int): The number of guesses the use took to win.
    """
    # Open the leaderboard in read-only mode.
    with open("leaderboard.csv", "r") as leaderboard:
        # Create a CSV reader.
        reader = csv.reader(leaderboard)
        # Sort rows by score in ascending order.
        sorted_rows = sorted(
            reader,
            key=lambda row: int(row[1]) if row[1].isdigit() else 0,
            reverse=False,
        )

        print("THE 10 BEST PLAYERS\n")
        print("INITIAL     SCORE")
        for i, row in enumerate(sorted_rows):
            print(row[0], "       ", row[1])

            if i == 9:
                break

        print("\nPress <enter> to return")
        input()

    main_menu(name)


def typewriter(text, delay=0.04):
    """
    Create a typewrite effect for print statements.

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

# Get the user's initials.
name = check_name()

# Run main menu.
main_menu(name)

# Run logic for the game.
game_code(name)


print("\nG A M E   O V E R")
