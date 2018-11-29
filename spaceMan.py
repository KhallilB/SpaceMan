import random

#Get Players Name
name = input("Tell me your name: ")

#Welcome Message
print("Hello " + name + "! Welcome to SpaceMan. Lets start playing!") 

#Getting Words To Import
def wordsToGuess():
    #Opens Text File
    file = open('wordsToGuess.txt', 'R')
    #Reads the lines in the text file and splits them
    wordsList = file.split()
    file.close()
    #chooses a random word and returns it
    hiddenWord = random.choice(wordsList)
    return hiddenWord

def turns(hiddenWord, letterGuessed):
    #gets the amount of guesses
    round = 0 
    for i in hiddenWord:
        if i in letterGuessed:
            round += 1
    if round == len(hiddenWord):
        return True
    else:
        return False

 b
# def getGuessedLetters(hiddenWord, letterGuessed):
#     #creates an underscore of if word isnt already guessed
#     string = ""
#     for i in hiddenWord:
#         if i in letterGuessed:
#             string += 1
#         else:
#             string += "_ "
#         return string

# def lettersToGuess(letterGuessed):
#     #String of letters that havent been guessed appends them to an empty string
#     string = ""
#     letters  = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
#     for i in letters:
#         for i not in letterGuessed:
#             string += 1
#     return string


