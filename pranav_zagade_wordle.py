from pranav_zagade_ui import Ui
import pranav_zagade_dictionary as dictionaryClass
from pranav_zagade_letterfrequency import CalculateStatistics
from typing import Dict, List, Tuple
from pranav_zagade_Word_Finder import Helper
import Database


class Wordle:
    def __init__(self) -> None:
        self.dictionary = dictionaryClass.Dictionary()

    def __str__(self) -> None:
        return "Main Game class"

    # Initialise all variables
    def initVariables(self, words_used: List[str]) -> Tuple[str, List, List, str, int, List, str, str]:
        todays_word, word_list = self.dictionary.getRandomWord(words_used)
        # print(str(self.dictionary))
        words_used.append(todays_word)
        entered_words = []
        answer = [None, None, None, None, None]
        attempt = 0
        good_letters = ""
        bad_letters = ""
        # print(todays_word)
        return todays_word, word_list, entered_words, answer, attempt, words_used, good_letters, bad_letters

    def main(self):

        words_used = []
        todays_word, word_list, entered_words, answer, attempt, words_used, good_letters, bad_letters = self.initVariables(
            words_used)
        games_played = 0
        games_won = 0
        guess_history = []

        while attempt < 6:
            if games_played == 1000:
                break
            # input_word = Ui.inputFromUser(attempt)
            new_answer = ""
            if all(v is not None for v in answer):
                for char in answer:
                    if char == "`" or char == '"':
                        new_answer += " "
                    else:
                        new_answer += char
            input_word = Helper.help(
                good_letters, bad_letters, new_answer, entered_words)

            # print(f"Attempt {attempt+1} : {input_word}\n")

            # if empty word entered then quit playing
            if(len(input_word.strip()) == 0):
                print("\nThank you for Playing.!")
                print("\nExiting")
                self.displayResults(games_played, games_won, guess_history)
                break

            # check if entered word is having any special characters
            if(not Ui.checkInput(input_word)):
                continue

            # check if entered word has already been entered before
            if(not Ui.checkWordUsed(input_word, entered_words)):
                continue

            # check if entered word is of length 5
            if(not Ui.checkWordLength(input_word)):
                continue

            # check if word was entered previously
            if(input_word not in word_list):
                print("\nEntered word not in dictionary!")
                continue

            # check if the guess is correct
            if input_word == todays_word:
                print(
                    f"Hurray !!!\nYou correctly guessed today's word: {todays_word}")

                games_played += 1
                games_won += 1
                guess_history.append(attempt+1)
                self.displayResults(games_played, games_won, guess_history)
                Database.everyGameDb(
                    games_played, todays_word, attempt, "Successful", " ".join(entered_words))
                todays_word, word_list, entered_words, answer, attempt, words_used, good_letters, bad_letters = self.initVariables(
                    words_used)
                # print("Starting a New Game, Press enter to exit")
                continue
                # break

            letter_counts = {}

            # Generate a dictionary to store letter count
            for letter in todays_word:
                if letter in letter_counts.keys():
                    letter_counts[letter] += 1
                else:
                    letter_counts[letter] = 1

            # comparing the characters of input_word and todays_word in corresponding position
            for index in range(len(input_word)):
                if input_word[index] == todays_word[index]:
                    answer[index] = todays_word[index]
                    letter_counts[todays_word[index]] -= 1
                    if input_word[index] not in good_letters:
                        good_letters += input_word[index]
                else:
                    answer[index] = '"'

            # checking which characters of input_word are present and absent in todays_word
            for index in range(len(input_word)):
                if input_word[index] != todays_word[index]:
                    if input_word[index] in letter_counts:
                        if letter_counts[input_word[index]] > 0:
                            letter_counts[input_word[index]] -= 1
                            answer[index] = "`"
                            if input_word[index] not in good_letters:
                                good_letters += input_word[index]
                    else:
                        if input_word[index] not in bad_letters:
                            bad_letters += input_word[index]

            entered_words.append(input_word)
            attempt += 1

            # print(f"The good letters selected: " + good_letters)
            # print(f"The bad letters selected : " + bad_letters + "\n")

            if attempt == 6:
                print(f"Hard luck!!!\nToday's word was {todays_word}")
                games_played += 1
                self.displayResults(games_played, games_won, guess_history)
                Database.everyGameDb(
                    games_played, todays_word, -1, "Unsuccessful", " ".join(entered_words))
                todays_word, word_list, entered_words, answer, attempt, words_used, good_letters, bad_letters = self.initVariables(
                    words_used)
                # print("Starting a New Game, Press enter to exit")
                # break
                continue

    def displayResults(self, games_played: int, games_won: int, guess_history: List[str]) -> None:
        print(f"\nNumber of Games Played : {games_played}")


if __name__ == "__main__":
    Database.truncateWordle()
    game = Wordle()
    game.main()
    print()
    print("**********************************************DATABASE CONTENT**********************************************")
    Database.queryWordle()
    Database.calcStats()
    stats = CalculateStatistics()
    stats.calculateAndSortWords()
