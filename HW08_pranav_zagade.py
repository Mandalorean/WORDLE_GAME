import csv
import string


class occurence:
    
    def __init__(self):
        pass

    occurence_stat = dict( (key, [0,0,0,0,0]) for key in string.ascii_lowercase )
       
    def check_likelihood_range(likelihood):
        if likelihood<1:
            return True
        else:
            return False
        
    #to check if the word length is 5
    def check_len(given_wrd):
        if len(given_wrd) == 5:
            return True
        else:
            return False
            
    #For calculating the letter likelihood
    def frequency_letter():
        occurence_stat = dict( (key, [0,0,0,0,0]) for key in string.ascii_lowercase )
        filtered_word_list = []
        p = open("filtered_dict.txt", "r")
        word_file = p.read()
        word_list = word_file.split("\n")
        filtered_word_list = list(word_list)
        p.close()
        for given_wrd in filtered_word_list:
            count = 0
            for alphabet in given_wrd:
                occurence_stat[alphabet][count] += 1
                count+=1
        
        for alphabet in string.ascii_lowercase:
            value = 0
            for given_wrd in filtered_word_list:
                value += 1
            for i in range(5):
                occurence_stat[alphabet][i] = round((occurence_stat[alphabet][i] / value),4)

        f = open("letterFrequency.csv", 'w')
        for alphabet in string.ascii_lowercase:
            f.write(f"{alphabet}, {occurence_stat[alphabet][0]}, {occurence_stat[alphabet][1]}, {occurence_stat[alphabet][2]}, {occurence_stat[alphabet][3]}, {occurence_stat[alphabet][4]}\n")

        return occurence_stat


    #for calculating word occurence Likelihood      
    def occurence_rank_words():
        occurence_stat = dict( (key, [0,0,0,0,0]) for key in string.ascii_lowercase )
        filtered_word_list = []
        occ_like = {}
        p = open("filtered_dict.txt", "r")
        word_file = p.read()
        word_list = word_file.split("\n")
        filtered_word_list = list(word_list)
        p.close()
        for given_wrd in filtered_word_list:
            if occurence.check_len(given_wrd):
                occurence_likelihood = float(occurence_stat[given_wrd[0]][0]) * float(occurence_stat[given_wrd[1]][1]) * float(occurence_stat[given_wrd[2]][2]) * float(occurence_stat[given_wrd[3]][3]) * float(occurence_stat[given_wrd[4]][4])
                if occurence.check_likelihood_range(occurence_likelihood):
                        occ_like[given_wrd] = occurence_likelihood

        sorted_list = sorted(occ_like.items(), key=lambda x:x[1])
        sorted_list.reverse()
        f = open("wordRank.csv", 'w')
        f.write("Rank, Word, Likelihood \n")
        value = 1
        for given_wrd in sorted_list:
            print(value)
            f.write(f"{value}, {given_wrd[0]}, {given_wrd[1]}\n")
            value += 1
        f.close()
        return sorted_list

    #Converting the list to Tuple
    def list_To_tuple(diction):
        for key in diction.keys():
            diction[key] = tuple(diction[key])
        return diction

    #Convert the Statistics into a Dictionary of Tuples
    def statsTodicTuples():
        file = open("letterFrequency.csv")
        csvreader = csv.reader(file)
        wrd_occurence_csv = {}
        for row in csvreader:
            wrd_occurence_csv[row[0]] = (row[1], row[2], row[3], row[4], row[5])
        #print(word_occurence_csv)
        file.close()
        return wrd_occurence_csv

    

    


    print(frequency_letter())
    print()
    print(list_To_tuple(occurence_stat))
    print()
    print(statsTodicTuples())
    print()
    print(occurence_rank_words())