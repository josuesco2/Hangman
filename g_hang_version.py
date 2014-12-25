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
LEVELS = set(['HARD','MEDIUM','EASY'])
WORDS = {
         'HARD':set(['eloquent','embezzle','deride']),
         'MEDIUM':set(['peculiar','unicode','bilateral','eclipse']),
         'EASY':set(['car', 'wonderful','atmosphere'])
        }

INSTRUCTIONS = '''
                Instructions: We will coose a word
                we will display how many characters
                are on the word, you ned to correctly
                provide the characters that belong to
                the hidden word.
                '''

def game_msg(level, len, word, tries, wrong):
    GAME_MESSAGE = '''
    HANGMAN:

        WORD:
              ({1}): {2}

        STATUS:
             LEVEL: {0}

             REMAINING TRIES: {3}

             WRONG CHAR: {4}
                   '''
    return GAME_MESSAGE.format(level, len, word, tries, wrong)

def word_selector(LVL):
    words = WORDS[LVL]
    return str(random.sample(words, 1)[0])

def tries_counter(tries):
    while True:
        yield tries
        tries  = tries - 1

def valid_char(char):
    return True if len(list(char)) == 1 else False

def board_status(word):
    return  ''.join(str(c) for c in word)

if __name__ == '__main__':

    print bcolors.FAIL, STAGES[0]
    print bcolors.WARNING, INSTRUCTIONS

    LEVEL = raw_input("Provide level to set the game: HARD, MEDIUM, EASY:  ")
    CURR_LEVEL = LEVEL.upper()

    if CURR_LEVEL in LEVELS:
        print "\n"
        print "Setting game level at %s" % (CURR_LEVEL)
        time.sleep(1)
        sys.stderr.write("\x1b[2J\x1b[H")
    else:
        sys.exit("Is this a joke('%s'), I only take HARD,MEDIUM AND EASY AS INPUT!!!.. I'M OUT" % (CURR_LEVEL))

    WRNG_CHARS = []
    CURR_WORD =  word_selector(CURR_LEVEL)
    CONF_WORD = list(CURR_WORD)
    WORD_LEN = len(CURR_WORD)
    WORD_TRACKER = ["*"]  * len(CURR_WORD)
    INIT_TRIES = 5
    TRIES_WATCHER = tries_counter(INIT_TRIES)


    print game_msg(CURR_LEVEL, WORD_LEN, board_status(WORD_TRACKER), INIT_TRIES, WRNG_CHARS)
    print bcolors.OKGREEN, STAGES[1]
    print "\n"
    print "--{ Provide one CHAR at a time! }--"

    INPUT_CHAR = raw_input("ENTER YOUR CHARACTER: ")
    if not valid_char(INPUT_CHAR):
       sys.exit("you obviously have a problem following instructions...I'M OUT")


