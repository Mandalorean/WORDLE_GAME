#By Pranav Zagade
#SSWv - 810 A
from typing import List
from alpha_position import alpha_pos
from HW03_Pranav_Zagade_wordle import Wordle
from colorama import Fore
import random


def main():

    puzzle_words = load_puzzle_set("HW03_Pranav_Zagade_dictionary.txt")
    puzzle = random.choice(list(puzzle_words))
    wordle = Wordle(puzzle)

    while wordle.user_can_attempt:
        print("Rules of the game: \n 1. A player must guess a random five-letter word. \n 2. You have 6 attempts to solve the game. \n 3. A letter in green means it’s correct and in the right place. A letter in yellow means it’s in the word but in the wrong place. \n 4. The word needs to be typed in all caps ")
        i = input("\n Guess the word: ")

        if len(i) != wordle.WORD_LENGTH:
            print(
                Fore.RED
                + f"Word has to be {wordle.WORD_LENGTH} spaces long!"
                + Fore.RESET
            )
            continue

        if not i in puzzle_words:
            print(
                Fore.RED
                + f"{i} is not valid. Retype a valid word!"
                + Fore.RESET
            )
            continue

        wordle.user_attempt(i)
        display_user_results(wordle)

    if wordle.is_passed:
        print("You have solved the puzzle.")
    else:
        print("You failed! ")
        print(f"The puzzle was: {wordle.puzzle}")


#to display the past attempts of the user
def display_user_results(wordle: Wordle):
    print("\nYour guesses so far...")
    print(f"Number of attempts remaining {wordle.user_attempts_remaining} .\n")

    border = []

    for user_word in wordle.user_attempts:
        user_result = wordle.past_user_guess(user_word)
        colored_result_str = convert_attempt_color(user_result)
        border.append(colored_result_str)

    for _ in range(wordle.user_attempts_remaining):
        border.append(" ".join(["_"] * wordle.WORD_LENGTH))

    ui_border(border)

#convert color of the  wrong position words and correct position words 
def convert_attempt_color(user_result: List[alpha_pos]):
    attempt_with_color = []
    for letter in user_result:
        if letter.correct_position:
            color = Fore.GREEN
        elif letter.wrong_pos:
            color = Fore.YELLOW
        else:
            color = Fore.WHITE
        colored_letter = color + letter.character + Fore.RESET
        attempt_with_color.append(colored_letter)
    return " ".join(attempt_with_color)
 
#to display results in a systematic box   
def ui_border(lines: List[str], size: int = 9, pad: int = 1):
    
    content_length = size + pad * 2
    top_border = "┌" + "─" * content_length + "┐"
    bottom_border = "└" + "─" * content_length + "┘"
    space = " " * pad
    print(top_border)

    for line in lines:
        print("│" + space + line + space + "│")

    print(bottom_border)

#to define the question word in the code
def load_puzzle_set(path: str):
    puzzle_words = set()
    with open(path, "r") as file:
        for line in file.readlines():
            question_word = line.strip().upper()
            puzzle_words.add(question_word)
    return puzzle_words








if __name__ == "__main__":
    main()
