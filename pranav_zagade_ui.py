# Get input from user
from typing import List

"""This class is just for validations hence it does not contain __init__ or __str__ or getters and setters"""


class Ui:
    def inputFromUser(attempt: int) -> str:
        input_word = input(
            f'\nAttempt {attempt+1} - Please enter a 5 character word : ').upper()
        return input_word

    # check if entered word is having any special characters

    def checkInput(input_word: str) -> bool:
        if input_word.isalpha() == False:
            print('\nWARNING : Please enter a word containing only Alphabets.')
            return False
        else:
            return True

    # check if entered word has already been entered before

    def checkWordUsed(input_word: str, entered_words: List[str]) -> bool:
        if input_word in entered_words:
            print(f'\nWARNING : {input_word} already entered once!!!')
            return False
        else:
            return True

    # check if entered word is of length 5

    def checkWordLength(input_word: str) -> bool:
        if len(input_word.strip()) != 5:  # To handle empty spaces strings like "     "
            print('\nWARNING : Word should be of length 5')
            return False
        else:
            return True
