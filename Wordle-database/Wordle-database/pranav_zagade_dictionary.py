import random
from typing import List, Tuple


class Dictionary:
    def __init__(self) -> None:
        self.myWordList = []
        self.finalWord = ""

    def __str__(self) -> str:
        return str(self.finalWord)

    # Getter
    def getter(self):
        return self.myWordList, self.finalWord

    # Setter
    def setter(self, inputWordList, inputfinalWord):
        self.myWordList = inputWordList
        self.finalWord = inputfinalWord

    # Return a random word of length 5 from given words file

    def getRandomWord(self, words_used: List[str]) -> Tuple[str, List]:
        try:
            f = open("words.txt", "r")
            new_file = open("new_words.txt", "w")

            for x in f:
                # words contain '\n' at the end which counts as 1 character, hence 6
                if(len(x) == 6 and x not in words_used):
                    self.myWordList.append(x[:-1].upper())
                    # writing to new file "new_file.txt"
                    new_file.write(f"{x.upper()}")

            # for item in words_used:
            #     if item in self.myWordList:
            #         self.myWordList.remove(item)

            if len(self.myWordList) == 0:
                for x in f:
                    if(len(x) == 6):  # words contain '\n' at the end which counts as 1 character, hence 6
                        self.myWordList.append(x[:-1].upper())

            word = random.choices(self.myWordList)
            for item in word:
                self.finalWord = item

            f.close()
            new_file.close()

        except IOError:
            print('An error occured trying to read the file.')
            print(
                'Please make sure "words.txt" is present in the directory before running the program')
            quit()
        else:
            return self.finalWord.upper(), self.myWordList
