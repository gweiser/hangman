from wonderwords import RandomWord
import re
import csv
import sys
import stages
from tabulate import tabulate
from colorama import Fore


def generate(length):
    """Generates a random word for the user"""
    r = RandomWord()
    return r.word(word_min_length=length, word_max_length=length)


def checkletter(letter, word):
    """Check if a proved letter is part of the word"""
    indices = []
    letterFound = False
    for w in word:
        # if a letter matches
        if w == letter:
            letterFound == True
            # Check how often letter occurs
            indices = [m.start() for m in re.finditer(letter, word)]
            return indices
        # if the letter is not in the word
        else:
            pass

    if not letterFound:
        raise ValueError


def updateStats(status):
    """Updates the wins/losses stats"""
    header = ["wins", "losses"]
    wins = 0
    losses = 0
    with open("stats.csv") as readfile:
        reader = csv.reader(readfile)
        next(reader)
        for line in reader:
            try:
                wins = int(line[0])
                losses = int(line[1])
            except IndexError:
                pass

    if status == 0:
        wins += 1
    else:
        losses += 1

    with open("stats.csv", "w") as writefile:
        writer = csv.writer(writefile)
        writer.writerow(header)
        writer.writerow([wins, losses])


def game():
    """Play a game of Hangman"""
    while True:
        try:
            # Get length of word
            length = int(input("Word length: "))
            break
        except ValueError:
            "If user inputs wrong data type"
            pass
    while str(length).isalpha() or int(length) < 2 or int(length) > 17:
        # Check for weird input
        print("Length must be larger than 1 and smaller than 18")
        length = input("Word length: ")

    # Generate word as specified
    word = generate(int(length)).lower()
    mistakes = 0
    wrongLetters = []

    # Create and print blank spaces
    blanks = ""
    for _ in range(len(word)):
        blanks += "_"
    # Print blanks in green
    print(Fore.GREEN + blanks)
    # Change text colour back to white
    print(Fore.WHITE)

    while mistakes < 8:
        try:
            # Make sure colour is white
            print(Fore.WHITE)
            # Get letter to check
            letter = input("Letter: ")
            # Filtering out blank input
            while letter.strip() == "":
                letter = input("Letter: ")
            # All indices where letter matches
            indices = checkletter(letter, word)
            # Replace blanks at the indices of the letter
            for i in indices:
                blanks = list(blanks)
                blanks[i] = letter
                blanks = "".join(blanks)
            if "_" not in blanks:
                updateStats(0)
                print(word)
                print("You win!")
                playAgain(input("Do you want to play again? [Y/N] ").lower())

            # Print blanks in green
            print(Fore.GREEN + blanks)
            # Change text colour back to white
            print(Fore.WHITE)
        except ValueError:
            # If letter is not in word
            if letter not in wrongLetters:
                wrongLetters.append(letter)
            mistakes += 1
            match mistakes:
                # Add a stage to hangman for each wrong input
                case 1:
                    print(stages.firstStage(wrongLetters))
                case 2:
                    print(stages.secondStage(wrongLetters))
                case 3:
                    print(stages.thirdStage(wrongLetters))
                case 4:
                    print(stages.fourthStage(wrongLetters))
                case 5:
                    print(stages.fifthStage(wrongLetters))
                case 6:
                    print(stages.sixthStage(wrongLetters))
                case 7:
                    print(stages.seventhStage(wrongLetters))
                case 8:
                    print(stages.eightStage(wrongLetters))
    # Update the stats
    updateStats(1)
    # Make sure colour is white
    print(Fore.WHITE)
    print(f"GAME OVER - word was {word}")
    # Ask player about further action
    playAgain(input("Do you want to play again? [Y/N] ").lower())


def stats():
    """Show user stats"""
    data = []
    with open("stats.csv") as file:
        reader = csv.reader(file)
        next(reader)
        for line in reader:
            data.append(line)

    table = tabulate(data, headers=["wins", "losses"])
    print(table)


def playAgain(s):
    """Determine if the player wants to play again"""

    # Filter input
    while s not in ["y", "n"]:
        s = input(
            "Do you want to play again? [Y/N] ").lower()

    if s == "y":
        # Play a game of Hangman
        game()
    else:
        # Ask if the user wants to see their stats
        seeStats = input(
            "Do you want to see your stats? [Y/N] ").lower()

        # Filter input
        while seeStats not in ["y", "n"]:
            seeStats = input(
                "Do you want to see your stats? [Y/N] ").lower()
        if seeStats == "y":
            stats()
            sys.exit("Good Bye!")
        else:
            sys.exit("Good Bye!")
