import csv
#helper function for wordle to search for words having the highest probablity using good alphabets and bad alphabets

#open the csv file
file = open("wordRank.csv")
csvreader = csv.reader(file)
header = next(csvreader)
rows = []
for row in csvreader:
    rows.append(row)

    
def main(good_words, bad_words):

    final_list = []
    good_words_list = []
    
    for row in rows:
        word = list(row[1].strip())
        
        #flags for 5 different positions
        letter_one_match = True
        letter_two_match = True
        letter_three_match = True
        letter_four_match = True
        letter_five_match = True
        
        if good_words[0] != '_':
            if good_words[0] != word[0]:
                letter_one_match = False
        
        if good_words[1] != '_':
            if good_words[1] != word[1]:
                letter_two_match = False
        
        if good_words[2] != '_':
            if good_words[2] != word[2]:
                letter_three_match = False
        
        if good_words[3] != '_':
            if good_words[3] != word[3]:
                letter_four_match = False
        
        if good_words[4] != '_':
            if good_words[4] != word[4]:
                letter_five_match = False
        
        #to check if the good words and their positions match
        if letter_one_match and letter_two_match and letter_three_match and letter_four_match and letter_five_match:
            good_words_list.append(row)
    
    #to remove the bad words from filtered list        
    for row in good_words_list:
        word = list(row[1].strip())
        
        match = list(set(word).intersection(set(bad_words)))
        
        if len(match) == 0:
            final_list.append(row)
        else:
            continue
    
    return final_list
    
good_pattern = list(input("Enter a pattern using good letters, and underscores for empty space, eg. '_r__e' :"))
bad_letters = list(input("Enter bad letters without space, eg. 'ap' :"))

if len(good_pattern) == 0:
    for i in range(50):
        print(rows[i][1].strip())
else:
    print(main(good_pattern, bad_letters))
