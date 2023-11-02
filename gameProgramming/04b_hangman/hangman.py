# Hangman Game by jahreem Jeffers v0.1
import random

words = 'tricky hank pico whitty tabi agoti matt sans paparus gaster steve alex pepinno aiden jaiden chrisly blaze melina jason max rex chara doomslayer kratos thor madmax void carol hex johnnycage'.split()

# VARIABLE_NAME in ALL-CAPS ARE CONSTANTS AND NOT MEANT TO CHANGE!
HANGMAN_BOARD = ['''
    +---+
        |
        |
        |
     ========''', '''
     +---+
     0  |
        |
        |
     ========''', '''
     +---+
     0  |
     |  |
        |
     ========''', '''
     +---+
     0  |
    /|  |
        |
     ========''', '''
    
     +---+
     0  |
    /|\ |
        |
     ========''', '''
     +---+
     0  |
    /|\ |
    /   |
     ========''', '''
     +---+
     0  |
    /|\ |
    / \ |
     ========''']
     
# Pick Word from List
def getRandomWord(wordList): # Return a random word from the list.
    wordIndex = random.randint(0,len(wordList)- 1)
    #len(listName - 1 is EXTREMELY COMMON FOR WORKING FOR LISTS.
    return wordList[wordIndex]
    
def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_BOARD[len(missedLetters)])
    print()
    
    print('Missed Letters:', end = ' ')
    for eachLetter in missedLetters:
        print(eachLetter, end = ' ')
    print()
    
    blanks = '_' * len(secretWord)
    
    # Replace Blanks with Correct Letters
    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:] 
            
    for letter in blanks:
        print(letter, end = ' ')
    print()


def getGuess(alreadyGuessed):
    while True:
        print('Please guess a letter and press enter.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('Letter has been guessed already, try again.')
        elif guess not in 'abcdefghijklmnopqurstuvwxyz':
            print('Please guess a LETTER from the English alphabet.')
        else:
            return guess

def playAgain():
    print('Do you want to play Again? Yes or No?')
    return input().lower().startswith('y')




#i = 0
#while i < 100:
    #word = getRandomWord(words)
    #print(word)
    #i += 1
    
    
