import string
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...

    alphabet_lowercase = string.ascii_lowercase
    alphabet_lowercase_list = []

    for char in alphabet_lowercase:
        alphabet_lowercase_list.append(char)
        for item in lettersGuessed:
            if item == char:
                alphabet_lowercase_list.remove(char)


    available_letters = " ".join(alphabet_lowercase_list)

    return available_letters

lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print(getAvailableLetters(lettersGuessed))
print(len(getAvailableLetters(lettersGuessed)))