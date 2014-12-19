#!/usr/bin/env python

import sys
import time
import random



STAGES = [
'''
      [[[[[[]
      []    |
      []    O
      []   /|' HANGMAN!
      []   //
      []  ``
      =============''',
'''
      [[[[[[]
      []
      []
      []
      []
      []
      =============''',
'''
      [[[[[[]
      []    |
      []
      []
      []
      []
      =============''',
'''
      [[[[[[]
      []    |
      []    O
      []    |
      []
      []
      =============''',
'''
      [[[[[[]
      []    |
      []    O
      []   /|'
      []
      []
      =============''',
'''
      [[[[[[]
      []    |
      []    O
      []   /|'
      []   //
      []
      =============''',
]


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

CLEAR = sys.stderr.write("\x1b[2J\x1b[H")
LEVELS = set('HARD','MEDIUM','EASY')
HARD = set('eloquent','embezzle','deride')
MEDIUM = set('peculiar','unicode','bilateral','eclipse')
EASY = set('automobile', 'microwaves','atmosphere')

INSTRUCTIONS = '''
                Instructions: We will coose a word
                we will display how many characters
                are on the word, you ned to correctly
                provide the characters that belong to
                the hidden word.
                '''

WORDS = ['peculiar','unicode','bilateral','eclipse']

if __name__ == '__main__':

    print bcolors.FAIL, STAGES[0]
    print bcolors.WARNING, INSTRUCTIONS
    LEVEL = raw_input("Provide level to set the game: HARD, MEDIUM, EASY:  ")
    if LEVEL.upper() in LEVELS:
        print "Setting game level at %s" % (LEVEL)
        time.sleep(2)
        sys.stderr.write("\x1b[2J\x1b[H")
    else:
        sys.exit("Is this a joke('%s'), I only take HARD,MEDIUM AND EASY AS INPUT!!!.. I'M OUT" % (LEVEL))

    random_word = LEVEL.u
    print random_word

