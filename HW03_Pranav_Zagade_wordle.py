from numpy import character
from alpha_position import alpha_pos


class Wordle:

    MAX_ATTEMPTS = 6
    WORD_LENGTH = 5

    def __init__(self, puzzle: str):
        self.puzzle: str = puzzle.upper()
        self.user_attempts = []

    def user_attempt(self, word: str):
        user_word = word.upper()
        self.user_attempts.append(user_word)
    
    #check if user has nay attempts left  
    @property
    def user_can_attempt(self):
        return self.user_attempts_remaining > 0 and not self.is_passed
    
    #to check if user passed    
    @property
    def is_passed(self):
        return len(self.user_attempts) > 0 and self.user_attempts[-1] == self.puzzle
    
    #to save the past user gusses
    def past_user_guess(self, user_word: str):
        user_word = user_word.upper()
        user_result = []
        for n in range(self.WORD_LENGTH):
            i = user_word[n]
            letter = alpha_pos(i)
            letter.is_in_word = i in self.puzzle
            letter.is_in_position = i == self.puzzle[n]
            user_result.append(letter)

        return user_result

    #user attempts remaining
    @property
    def user_attempts_remaining(self) -> int:
        return self.MAX_ATTEMPTS - len(self.user_attempts)

    
