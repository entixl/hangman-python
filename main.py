import random 
import json

GREEN = "\033[42m"  
YELLOW = "\033[43m" 
GRAY = "\033[100m"  
RESET = "\033[0m"

def main():
    with open("words.json" , "r") as f:
        words = json.load(f)
    difficulty_level = get_difficulty_level()
    rarity = get_rarity(difficulty_level)
    word = random.choice(words[rarity])
    print(word)
    wrong_guess = 0
    for i in range(6):
        display_word(word)
        if usr_input != word:
            wrong_guess +=  1

def get_guess(word):
    while True:
        try:
            guess = input("enter your guess: ")
            if len(guess) != len(word):
                raise ValueError("")



def wordle_display(secret, guess):
    display = ""
    for i, letter in enumerate(guess):
        if letter == secret[i]:
            display += GREEN + letter.upper()  + RESET
        elif letter in secret:
            display += YELLOW + letter.upper() + RESET
        else:
            display += GRAY + letter.upper() + RESET
    print(display)


wordle_display("apple", "arlie")

def draw_hangman(wrong_choices):
    hangman_art = {
        1: (" o ",
            "   ",
            "   "),
        2: (" o ",
            " | ",
            "   "),
        3: (" o ",
            "/| ",
            "   "),
        4: (" o ",
            "/|\\",
            "   "),
        5: (" o ",
            "/|\\",
            "/  "),
        6: (" o ",
            "/|\\",
            "/ \\")
    }
            
    for line in hangman_art[wrong_choices]:
        print("\t" , line)


def display_word(word):
        word_len = len(word)
        for _ in range(word_len):
            print("_" , end="")
        print("")


def get_difficulty_level():
    while True:
        try:
            difficulty_level= int(input(f"choose your difficulty level\n" 
                            "1.easy\n"
                            "2.normal\n" 
                            "3.hard\n"
                            "enter: "))
            if difficulty_level not in (1,2,3):
                raise ValueError("Choose 1,2 or 3")
        except ValueError:
            print("Enter either 1, 2 or 3")
        else:
            return difficulty_level


def get_rarity(difficulty_level):
    if difficulty_level == 1:
        return "common"
    elif difficulty_level ==2 :
        return "uncommon"
    else : 
        return "rare"
    
main()
