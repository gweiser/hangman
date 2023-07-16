from functions import game, stats
import stages
import sys
import csv


def main():
    menu = input(
        "Welcome to Hangman, press x to play or s to see your stats: ").lower()

    while menu not in ["x", "s"]:
        menu = input(
            "Welcome to Hangman, press x to play or s to see your stats: ").lower()

    if menu == "s":
        # Show stats
        stats()
        playgame = input(
            "Do you want to play a game of hangman? (Y/N): ").lower()

        while playgame not in ["y", "n"]:
            playgame = input(
                "Do you want to play a game of hangman? (Y/N): ").lower()
        if playgame == "y":
            game()
        elif playgame == "n":
            sys.exit()

    elif menu == "x":
        # Play game
        game()


if __name__ == "__main__":
    main()
