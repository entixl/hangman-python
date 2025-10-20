import json 
from random import choice

def game(total_words):
    difficulty_level = get_difficulty_level()
    rarity = get_rarity(difficulty_level)
    random_word = choice(total_words[rarity]).lower()
    display_intro(random_word , rarity)
    continue_game = True
    run_count = 0    
    total_results = []
    while continue_game :
        run_count += 1
        print(f"you have {6-run_count} guesses left")
        display_layout(random_word ,run_count, total_results)
        guess = get_guess(random_word)
        result , continue_game = evaluate_guess(random_word,guess , continue_game)
        total_results.append(result)
        if not continue_game:
            display_layout(random_word ,run_count, total_results)
            print("you win")
        if run_count > 6:
            print("you lost")
            print(f"the word was {random_word}")
            continue_game = False
def display_layout(random_word , run_count , total_result):
    if total_result :
        for result in total_result :
            print(result)
    for i in range(6 - run_count):
        for _ in random_word:
            print("-" , end="")
        print("")
def evaluate_guess(random_word,guess , continue_game):
    GREEN = "\033[42m"
    YELLOW = "\033[43m"
    RED = "\033[100m"
    RESET = "\033[0m"
    result = ""
    if random_word == guess :
        result += GREEN + guess + RESET
        continue_game = False
    for i ,letter in enumerate(guess):
        if letter == random_word[i]:
            result += GREEN + letter + RESET
        elif letter in random_word : 
            result += YELLOW + letter + RESET
        else : 
            result += RED + letter + RESET
    return (result , continue_game )

def get_guess(random_word):
    while True:
        try:
            guess = input("Enter your guess: ").lower()
            if len(guess) > len(random_word):
                raise ValueError(f"guess should be less than {len(random_word)}")
            elif len(guess) < len(random_word):
                for _ in range(len(random_word) - len(guess)):
                    guess += "-"
                return guess
            else :
                return guess
        except ValueError as e:
            print(e)
def get_rarity(difficulty_level):
    if difficulty_level == 1:
        return "easy"
    elif difficulty_level ==2 :
        return "normal"
    else : 
        return "hard"

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

def display_intro(word , rarity):
    length_word = len(word)
    msg = f"You have choosen {rarity}\nThe word have {length_word} letters"
    print(msg)
    for _ in range(23):
        print("X" , end="")
    print("")
    

if __name__ == "__main__":
    with open("words.json" ,"r") as f:
        total_words = json.load(f)
    game(total_words)