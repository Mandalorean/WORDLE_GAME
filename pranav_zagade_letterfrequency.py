# Function to calculate frequency of every letter in every position
from typing import Dict, List, Tuple


class CalculateStatistics:

    def calculateFrequencyOfLetters(self) -> None:
        try:
            f = open("new_words.txt", "r")

            data = {}
            data = {chr(new_list+65): [0, 0, 0, 0, 0]
                    for new_list in range(26)}
            count = 0
            for x in f:
                for i, item in enumerate(x):
                    if item != "\n":
                        data[item][i] += 1
                if x:
                    count += 1

            for key in data.keys():
                for item in range(5):
                    data[key][item] = round(data[key][item]/count, 3)
        except IOError:
            print('An error occured trying to read the file.')
            print(
                'Please make sure "new_words.txt" is present in the directory before running the program')
            quit()

        try:
            fs = open("letterFrequency.csv", "w")

            fs.write("letter,first_pos,second_pos,third_pos,fourth_pos,fifth_pos\n")
            for key in data.keys():
                answer = key
                for item in range(5):
                    answer += ","+str(data[key][item])
                fs.write(answer+",\n")

            fs.close()

        except IOError:
            print('An error occured trying to read the file.')
            print(
                'Please make sure "letterFrequency.csv" is present in the directory before running the program')
            quit()

    # convert the list containing frequency of letters to a tuple

    def convert_tuple(self, data: Dict[str, List]) -> Dict[str, Tuple]:
        new_data = {}

        for key in data.keys():
            new_data[key] = tuple(data[key])

        return new_data

    # read letterFrequency.csv and convert the list containing frequency to a tuple

    def read_and_make_tuple(self) -> Dict[str, tuple]:
        self.calculateFrequencyOfLetters()
        try:
            fsnew = open("letterFrequency.csv", "r")
            next(fsnew)
            answer = {}
            for x in fsnew:
                element = x.split(",")
                key = element[0]
                answer[key] = tuple(element[1:-1])

            fsnew.close()

        except IOError:
            print('An error occured trying to read the file.')
            print(
                'Please make sure "letterFrequency.csv" is present in the directory before running the program')
            quit()

        return answer

    # calculate weight of word, sort according to it and write to wordRank.csv

    def calculateAndSortWords(self) -> None:
        inputData = self.read_and_make_tuple()
        try:
            answer = {}

            f = open("new_words.txt", "r")
            for x in f:
                answer[x[:-1]] = 1
                for i, item in enumerate(x):
                    if item != '\n':
                        answer[x[:-1]] *= float(inputData[item][i])

            sorted_list = sorted(
                answer.items(), key=lambda x: x[1], reverse=True)

        except IOError:
            print('An error occured trying to read the file.')
            print(
                'Please make sure "new_words.txt" is present in the directory before running the program')
            quit()

        try:
            fs = open("wordRank.csv", "w")

            fs.write("word,value\n")

            for insideTuple in sorted_list:
                answer_new = insideTuple[0]
                answer_new += ","+str('{:.15f}'.format(insideTuple[1]))
                fs.write(answer_new+",\n")

            fs.close()
            f.close()

        except IOError:
            print('An error occured trying to read the file.')
            print(
                'Please make sure "wordRank.csv" is present in the directory before running the program')
            quit()
