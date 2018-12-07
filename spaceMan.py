import random
SPACEMAN = ['''
   +---+
   |   |
       |
       |
       |
       |
=========''', '''
   +---+
   |   |
   O   |
       |
       |
       | 
=========''', '''
   +---+
   |   |
   O   |
   |   |
       |
       |
=========''', '''
   +---+
   |   |
   O   |
  /|   |
       |
       |
=========''', '''
   +---+
   |   |
   O   |
  /|\  |
       |
       |
=========''', '''
   +---+
   |   |
   O   |
  /|\  |
  /    |
       |
=========''', '''
  +---+
   |   |
   O   |
  /|\  |
  / \  |
       |
=========''']


words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()


def getRandomWord(wordList):
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]


def showGame(SPACEMAN, wrongLetter, correctLetter, secretWord):
    print(SPACEMAN[len(wrongLetter)])
    print()

    print('Wrong Letters:', end='')
    for letter in wrongLetter:
        print(letter, end='')
    print()

    blanks = '_'*len(secretWord)

    for i in range(len(secretWord)):
        if secretWord[i] in correctLetter:
            blank = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks:
        print(letter, end='')
    print()


def getGuess(alreadyGussesed):
    while True:
        print('Guess a letter')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Enter one letter')
        elif guess in alreadyGussesed:
            print('You have already guessed that.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a Letter')
        else:
            return guess


def playAgain():
    print('Do you want to play again? (Yes or No)')
    return input().lower().startswith('y')


print('S P A C E M A N')
wrongLetter = ''
correctLetter = ''
secretWord = getRandomWord(words)
gameIsDone = False

while True:
    showGame(SPACEMAN, wrongLetter, correctLetter, secretWord)

    guess = getGuess(wrongLetter + correctLetter)

    if guess in secretWord:
        correctLetter = correctLetter + guess

        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetter:
                foundAllLetters = False
                break
        if foundAllLetters:
            print("You Win!")
    else:
        wrongLetter = wrongLetter + guess

        if len(wrongLetter) == len(SPACEMAN) - 1:
            showGame(SPACEMAN, wrongLetter, correctLetter, secretWord)
            print('You have run out of guesses!\nAfter ' + str(len(wrongLetter)) + ' missed guesses and ' +
                  str(len(correctLetter)) + ' correct guesses, the word was "' + secretWord + '"')
            gameIsDone = True

    if gameIsDone:
        if playAgain():
            wrongLetter = ''
            correctLetter = ''
            gameIsDone = False
            secretWord = getRandomWord(words)
        else:
            break
