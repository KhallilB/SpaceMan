import random


def loadWords():
    '''
    Loads words from txt files,
    splits them and chooses a random one.
    '''
    file = open('wordsToGuess.txt', 'r')
    line = file.readline()
    wordList = line.split()
    file.close()
    secretWord = random.choice(wordList)
    return secretWord


def userGuesses(correctGuess, wrongGuess, secretWord):
    '''
    Uses secret word to Guess.
    Displays the number of letters correct,
     and incorrect letter guesses.
    '''
    print([len(wrongGuess)])

    print('Wrong Guesses', end='')
    for letter in wrongGuess:
        print(letter, end='')

    blanks = ' ' * len(secretWord)

    for i in range(len(secretWord)):
        if secretWord[i] in correctGuess:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks:
        print(letter, end='')

    print()


def guessedWord():
    'Gets user letter guess entered.'
    pass


def playAgain():
    'Function allows user to play again, otherwise returns false'
    pass
