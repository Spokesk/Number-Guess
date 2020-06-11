import sys
from random import randint

level_difficulty = {
    "Easy": {
        'max_number': 10,
        'tries': 3
    },
    "Medium": {
        'max_number': 50,
        'tries': 5
    },
    "Hard": {
        'max_number': 100,
        'tries': 5
    },
    "Extreme": {
        'max_number': 1000,
        'tries': 3
    },
}


def choose_difficulty():
    choices = ("Easy", "Medium", "Hard", "Extreme")
    difficulty = input(
        "Choose your difficulty: Easy, Medium, Hard, Extreme: ").lower().capitalize()

    if difficulty in choices:
        return difficulty
    else:
        print("YOU DO NOT LISTEN! YOU ARE HEREBY BANNED!!!!")
        sys.exit(0)


def generate_number(max_number):
    return randint(1, max_number)


def player_guess(max_number, attempts):
    try:
        guess = int(input(
            "Choose a number between: 1-%d, attempts remaining: %d\n" % (max_number, attempts)))
    except:
        print("You imbecile, enter a number... ")

    if 0 < guess <= max_number:
        return guess
    else:
        print("I do not have time for people who DO NOT LISTEN!!!")
        sys.exit(0)
# sys.exit can be assigned an error code

def game_start():
    print("Welcome to the land where gamblers can become heroes!\n")

    difficulty = choose_difficulty()
    cpu_number = generate_number(level_difficulty[difficulty]["max_number"])

    counter = 0
    while True:
        guess = player_guess(
            level_difficulty[difficulty]["max_number"],
            level_difficulty[difficulty]["tries"] - counter
        )

        # check guess
        if guess < cpu_number:
            print("TOO LOW\n")
        elif guess > cpu_number:
            print("TOO HIGH\n")
        else:
            print(
                "\nYou have become the hero nobody wanted, but the hero everyone needed.\n")
            break

        # check remain attempts
        if level_difficulty[difficulty]["tries"] > counter:
            counter += 1
        else:
            print("Sorry, you are out of attempts")
            break

    again = input("Would you like to play again? Yes/No ").lower().capitalize()

    if again == "Yes" or again == "Y":
        print("Let's do it! \n")
        game_start()
    elif again == "No" or again == "N":
        print("Bye!\n")
    else:
        print("SCREW YOU! YOU ARE HEREBY BANNED!!!!")
        sys.exit()


game_start()
