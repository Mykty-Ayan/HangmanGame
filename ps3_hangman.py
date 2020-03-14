# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string
WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    flag = False
    secret_list = list(secretWord)
    compare_list = []
    for letter in lettersGuessed:
        if letter in secretWord:
            compare_list.append(letter)
    unique_secret_list = []
    for item in secret_list:
        if item not in unique_secret_list:
            unique_secret_list.append(item)
    if sorted(unique_secret_list) == sorted(compare_list):
        flag = True
    return flag


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
                if item in alphabet_lowercase_list:
                    alphabet_lowercase_list.remove(char)


    available_letters = " ".join(alphabet_lowercase_list)

    return available_letters


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    lives_available = 8
    letters_guessed = []

    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is ', len(secretWord), ' letters long.')
    while lives_available > 0 and not isWordGuessed(secretWord, letters_guessed):
        print('-------------')
        print('You have ', lives_available, ' guesses left.')
        print('Available letters: ', getAvailableLetters(letters_guessed))
        guess = input('Please guess a letter: ').lower()

        if guess in list(secretWord):
            letters_guessed.append(guess.lower())
            print('Good guess: ', getGuessedWord(secretWord, letters_guessed))
        elif guess in letters_guessed:
            print("Oops! You've already guessed that letter: ", getGuessedWord(secretWord, letters_guessed))
        else:
            letters_guessed.append(guess.lower())
            print("Oops! That letter is not in my word: ", getGuessedWord(secretWord, letters_guessed))
            lives_available -= 1
    if isWordGuessed(secretWord,letters_guessed):
        print('------------')
        print('Congratulations, you won!')
    else:
        print('-------------')
        print('Sorry, you ran out of guesses. The word was else. ')


        # When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
