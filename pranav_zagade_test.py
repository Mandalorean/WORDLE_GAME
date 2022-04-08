from pranav_zagade_ui import Ui
import HW03_pranav_zagade as dictionaryClass
from HW03_pranav_zagade_wordle import Wordle


def test_both_empty():
    result = Ui.checkInput("sonar")
    assert(result == True)


def test_upper():
    result = Ui.checkInput("SONAR")
    assert(result == True)


def test_empty():
    result = Ui.checkInput("")
    assert(result == False)


def test_num():
    result = Ui.checkInput("12345")
    assert(result == False)


def test_multiple_words():
    result = Ui.checkInput("Hello World")
    assert(result == False)


def test_word_used_one():
    result = Ui.checkWordUsed(
        "sonar".upper(), ["SONAR", "HELLO", "YEMEN", "COULD", "YACHT"])
    assert(result == False)


def test_word_used_two():
    result = Ui.checkWordUsed(
        "SONAR".upper(), ["SONAR", "HELLO", "YEMEN", "COULD", "YACHT"])
    assert(result == False)


def test_word_used_three():
    result = Ui.checkWordUsed(
        "SHIFT", ["SONAR", "HELLO", "YEMEN", "COULD", "YACHT"])
    assert(result == True)


def test_word_used_four():
    result = Ui.checkWordUsed(
        "", ["SONAR", "HELLO", "YEMEN", "COULD", "YACHT"])
    assert(result == True)


def test_word_length_one():
    result = Ui.checkWordLength(
        "     ")
    assert(result == False)


def test_word_length_two():
    result = Ui.checkWordLength(
        "")
    assert(result == False)


def test_word_length_three():
    result = Ui.checkWordLength(
        "SONAR")
    assert(result == True)


def test_word_length_three():
    result = Ui.checkWordLength(
        "SON")
    assert(result == False)


def test_word_length_three():
    result = Ui.checkWordLength(
        "SONARSONARSONAR")
    assert(result == False)


def test_dict_word_length():
    todays_word, word_list = dictionaryClass.Dictionary().getRandomWord([
        "YACHT"])
    assert(len(todays_word) == 5)


def test_word_in_dict():
    todays_word, word_list = dictionaryClass.Dictionary().getRandomWord([
        "YACHT"])
    assert(todays_word in word_list)


def test_word_dict_isUpper():
    todays_word, word_list = dictionaryClass.Dictionary().getRandomWord([
        "YACHT"])
    assert(todays_word.isupper())


def test_divide_by_zero():
    game = Wordle()
    assert(game.displayResults(0, 0, []) == None)
