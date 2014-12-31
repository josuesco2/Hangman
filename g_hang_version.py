#!/usr/bin/env python

import sys
import os
import time
import random

STAGES = [
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
'''
      [[[[[[]
      []    |
      []    O
      []   /|' HANGMAN!
      []   //
      []  ``
      =============''',

]


class bcolors:
    TEXT = '\033[1;36m'
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

def CLEAR():
    sys.stderr.write("\x1b[2J\x1b[H")

LEVELS = set(['HARD','MEDIUM','EASY'])
WORDS = {
         'HARD':set(['eloquent','embezzle','deride']),
         'MEDIUM':set(['peculiar','unicode','bilateral','eclipse']),
         'EASY':set(['car', 'wonderful','atmosphere'])
        }

INSTRUCTIONS = '''
                Instructions: We will choose a word
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

def stage_counter(stages):
    for stage in stages:
        yield stage

def int_test(char):
    try:
        int(char)
        return True
    except:
        return False

def valid_char(char):
    return True if len(list(char)) == 1 and not int_test(char) else False

def board_status(word):
    return  ''.join(str(c) for c in word)

def correct_char(char):
    return True if char in CONF_WORD else False

def display_corr(pst_obj):
    loc = pst_obj.values()[0]
    for key in loc:
        WORD_TRACKER[key] = pst_obj.keys()[0].upper()

class game_engine:

    def __init__(self, word):
        self.key_word = word
        self.parse_word = list(self.key_word)

    def test_char(self, char):
        return True if char in self.parse_word else False

    def clean_spot(self, pst):
        self.parse_word[pst] = None

    def char_mapper(self, char):
        obj = {char : []}
        self.counter = self.parse_word.count(char)
        while self.counter > 0:
            position = self.parse_word.index(char)
            obj[char].append(position)
            self.clean_spot(position)
            self.counter = self.counter - 1
        return obj

if __name__ == '__main__':

    print bcolors.FAIL, STAGES[5]
    print bcolors.TEXT, INSTRUCTIONS

    LEVEL = raw_input("Provide level to set the game: HARD, MEDIUM, EASY:  ")
    CURR_LEVEL = LEVEL.upper()

    if CURR_LEVEL in LEVELS:
        print "\n"
        print "Setting game level at %s" % (CURR_LEVEL)
        time.sleep(1)
        CLEAR()
    else:
        sys.exit("Is this a joke('%s'), I only take HARD,MEDIUM AND EASY AS INPUT!!!.. I'M OUT" % (CURR_LEVEL))

    CURR_WORD =  word_selector(CURR_LEVEL)
    WORD_LEN = len(CURR_WORD)
    WORD_TRACKER = ["*"]  * len(CURR_WORD)
    INIT_TRIES = 5
    WRNG_CHARS = []
    TRIES_WATCHER = tries_counter(INIT_TRIES)
    game_worker = game_engine(CURR_WORD)
    STAGE_WATCHER = stage_counter(STAGES)
    CURRENT_STAGE = STAGE_WATCHER.next()
    CURRENT_TRIES = TRIES_WATCHER.next()

    while True:
        print game_msg(CURR_LEVEL, WORD_LEN, board_status(WORD_TRACKER), CURRENT_TRIES, WRNG_CHARS)
        print bcolors.OKGREEN, CURRENT_STAGE
        print "\n"
        print "--{ Provide one CHAR at a time! }--"

        INPUT_CHAR = raw_input("ENTER YOUR CHARACTER: ")
        if not valid_char(INPUT_CHAR):
            sys.exit("you obviously have a problem following instructions...I'M OUT")

        CHAR = INPUT_CHAR.lower()
        if game_worker.test_char(CHAR):
            print bcolors.TEXT, "well done"
            display_corr(game_worker.char_mapper(CHAR))
            CLEAR()
            if '*' not in WORD_TRACKER:
                print "GREAT JOB, YOU WON"
                break
            print game_msg(CURR_LEVEL, WORD_LEN, board_status(WORD_TRACKER), CURRENT_TRIES, WRNG_CHARS)
            print bcolors.OKGREEN, CURRENT_STAGE
        else:
            CLEAR()
            print bcolors.TEXT, "incorrect..."
            WRNG_CHARS.append(CHAR)
            try:
                CURRENT_TRIES = TRIES_WATCHER.next()
                CURRENT_STAGE = STAGE_WATCHER.next()
                if CURRENT_TRIES == 0:
                    raise ValueError('Zero')
                time.sleep(1)
                os.system('clear')
                print bcolors.TEXT, game_msg(CURR_LEVEL, WORD_LEN, board_status(WORD_TRACKER), CURRENT_TRIES, WRNG_CHARS)
                print bcolors.HEADER, CURRENT_STAGE
            except:
                print bcolors.TEXT, game_msg(CURR_LEVEL, WORD_LEN, board_status(WORD_TRACKER), CURRENT_TRIES, WRNG_CHARS)
                print bcolors.FAIL, STAGES[5]
                print "GAME OVER!! YOU LOST"
                break
