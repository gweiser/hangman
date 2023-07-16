from colorama import Fore


def firstStage(letters):
    print(Fore.RED)
    stage = """

        |
        |
        |
    
    """
    allLetters = ""
    for i in letters:
        allLetters += i
    return stage + allLetters


def secondStage(letters):
    print(Fore.RED)
    stage = """
         _____
        |
        |
        |
    
    """
    allLetters = ""
    for i in letters:
        allLetters += i
    return stage + allLetters


def thirdStage(letters):
    print(Fore.RED)
    stage = """
         _____
        |/
        |
        |
    
    """
    allLetters = ""
    for i in letters:
        allLetters += i
    return stage + allLetters


def fourthStage(letters):
    print(Fore.RED)
    stage = """
         _____
        |/   |
        |    
        |
    
    """
    allLetters = ""
    for i in letters:
        allLetters += i
    return stage + allLetters


def fifthStage(letters):
    print(Fore.RED)
    stage = """
         _____
        |/   |
        |    O
        |
    
    """
    allLetters = ""
    for i in letters:
        allLetters += i
    return stage + allLetters


def sixthStage(letters):
    print(Fore.RED)
    stage = """
         _____
        |/   |
        |    O
        |    |
             |
    
    """
    allLetters = ""
    for i in letters:
        allLetters += i
    return stage + allLetters


def seventhStage(letters):
    print(Fore.RED)
    stage = """
         _____
        |/   |
        |    O
        |    |
             |
             ^
    
    """
    allLetters = ""
    for i in letters:
        allLetters += i
    return stage + allLetters


def eightStage(letters):
    print(Fore.RED)
    stage = """
         _____
        |/   |
        |    O
        |   \|/
             |
             ^
    
    """
    allLetters = ""
    for i in letters:
        allLetters += i
    return stage + allLetters
