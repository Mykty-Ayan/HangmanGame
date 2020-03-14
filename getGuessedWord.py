def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    secretList = []
    start = 0
    while start < len(secretWord):
        secretList.append('_')
        start += 1

    counter = 0
    for char in secretWord:
        for item in lettersGuessed:
            if item == char:
                secretList[counter] = item
        counter += 1

    hide = " ".join(secretList)

    return hide


secretWord = 'apple'
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print(getGuessedWord(secretWord, lettersGuessed))
