class Helper:

    def help(good_letters, bad_letters, new_answer, entered_words):

        goodWords = good_letters.upper()

        if len(goodWords) > 5:
            raise Exception("You can only have 5 good letters")

        goodWords = list(goodWords.strip())

        badWords = bad_letters.upper()

        badWords = list(badWords.strip())

        if any(x in goodWords for x in badWords):
            raise Exception('Letter cannot be both good and bad!\n')

        positionWords = new_answer.upper()
        if len(positionWords) != 0:
            if len(positionWords) != 5:
                raise Exception(
                    'Word should be of length 5 or empty\n')

        if not all(x.isalpha() or x.isspace() for x in positionWords):
            raise Exception(
                'Please enter a word containing only Alphabets or Spaces.\n')

        try:
            fs = open("wordRank.csv", "r")
            next(fs)

            wordlist = []
            tentative = []

            for x in fs:
                wordlist.append(x[0:5])

            # If user does not provide Good or bad words, then display top 50 words
            if len(goodWords) == 0 and len(badWords) == 0:
                return wordlist[0]

            for x in wordlist:
                # good = all(letter in x for letter in goodWords)
                goodflag = True
                badFlag = True
                for y in goodWords:
                    if y not in x:
                        goodflag = False
                        break
                for z in badWords:
                    if z in x:
                        badFlag = False

                if goodflag and badFlag:
                    tentative.append(x)

            copyTentative = tentative[:]

            if(len(positionWords) == 5):
                for x in tentative:
                    for index in range(5):
                        if positionWords[index] != " " and positionWords[index] != x[index]:
                            copyTentative.remove(x)
                            break

            fs.close()
        except IOError:
            print('An error occured trying to read the file.\n')
            print(
                'Please make sure "wordRank.csv" is present in the directory before running the program\n')
            quit()

        for word in entered_words:
            if word in copyTentative:
                copyTentative.remove(word)

        return copyTentative[0]
