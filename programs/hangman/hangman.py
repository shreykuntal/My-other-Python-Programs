# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "C:/Users/Shrey/Documents/python/programs/words.txt"

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

def correctguess(file):
  import pygame
  pygame.mixer.init()
  pygame.mixer.music.load(file)
  pygame.mixer.music.play()

def wrongguess(file):
  import pygame
  pygame.mixer.init()
  pygame.mixer.music.load(file)
  pygame.mixer.music.play()

def won(file):
  import pygame
  pygame.mixer.init()
  pygame.mixer.music.load(file)
  pygame.mixer.music.play()

def lost(file):
  import pygame
  pygame.mixer.init()
  pygame.mixer.music.load(file)
  pygame.mixer.music.play()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    words = 0
    while True:
      for letter in lettersGuessed:
        if letter in secretWord:
          words += secretWord.count(letter)
      break
    if words == len(secretWord):
      return True
    return False

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    toReturn = len(secretWord) * '_ '
    toReturn = list(toReturn)
    for letter in lettersGuessed:
      if letter in secretWord:
        for i in range(len(secretWord)):
          if secretWord[i] == letter:
            toReturn[i*2] = secretWord[i]
    toReturnstr = ''
    for x in toReturn:
      toReturnstr += x
    return toReturnstr

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    alpha_lower = list(string.ascii_lowercase)
    for letter in lettersGuessed:
      alpha_lower.remove(letter)
    alpha_lower_str = ''
    for letter in alpha_lower:
      alpha_lower_str += letter
    return alpha_lower_str
    
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
    import time
    import pygame 
    import os
    os.system('cls')
    import string
    print('Welcome to the game, Hangman!\n')
    print('I am thinking of a word that is %d letters long.' % (len(secretWord)))
    GuessesLeft = 8
    mistakesMade = 0
    lettersGuessed = []
    while True:
      if GuessesLeft == 0:
          print('Oops! That letter is not in my word: %s' % (getGuessedWord(secretWord, lettersGuessed)))
          print('--------\nSorry you ran out of guesses. The word was %s' % (secretWord))
          mistakesMade += 1 
          lost('C:/Users/Shrey/Documents/python/programs/hangman/lost.mp3')
          time.sleep(6)
          break
      print('--------\nYou have %d guesses left. Available letters %s' % (GuessesLeft, getAvailableLetters(lettersGuessed)))
      while True:
        user_guess = input('Please guess a letter: ').lower()
        if user_guess not in list(string.ascii_lowercase):
          print('-----\nPlease enter something relevant.\n')
          wrongguess('C:/Users/Shrey/Documents/python/programs/hangman/wrong guess.mp3')
          continue
        else:
          break
      if user_guess in lettersGuessed:
        wrongguess('C:/Users/Shrey/Documents/python/programs/hangman/wrong guess.mp3')
        print('Oops! You\'ve already guessed that letter: %s' % (getGuessedWord(secretWord, lettersGuessed)))
        continue
      lettersGuessed += [user_guess]
      if user_guess in secretWord:
        if isWordGuessed(secretWord, lettersGuessed):
          won('C:/Users/Shrey/Documents/python/programs/hangman/won.mp3')
          print('Good guess: %s' % (getGuessedWord(secretWord, lettersGuessed)))
          print('--------\nCongratulations, you won!')
          time.sleep(2)
          break
        else:
          correctguess('C:/Users/Shrey/Documents/python/programs/hangman/correct guess.mp3')
          print('Good guess: %s' % (getGuessedWord(secretWord, lettersGuessed)))
          continue
      else:
          wrongguess('C:/Users/Shrey/Documents/python/programs/hangman/wrong guess.mp3')
          GuessesLeft -= 1
          mistakesMade += 1
          if GuessesLeft == 0:
            continue
          print('Oops! That letter is not in my word: %s' % (getGuessedWord(secretWord, lettersGuessed)))
          
while True:
  secretWord = chooseWord(wordlist).lower()
  hangman(secretWord)
  ask = input('\n--------\n(y) to play or any other key to exit: ')
  if ask.lower() == 'y':
    continue
  else:
    print('\nThanks for playing!')
    break