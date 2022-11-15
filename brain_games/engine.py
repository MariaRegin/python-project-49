#!/usr/bin/env python3

import prompt
import random


name = prompt.string('May I have your name? ')

def welcome_user():
    print('Hello, ' + name + '!')

def explain_details(task):
    print(task)

def launch_game(operation, res):
    tries = 0
    while tries < 3:
        tries += 1
        print('Question: ', operation)
        answer = prompt.string('Your answer: ')

        if res == answer:
            print('Correct!')

        if res != answer:
            print('\"' + answer + '\"' + ' is wrong answer ;(. Correct answer was ' + res + '.' + "\nLet's try again, " + name + '!')
            break

    if tries >= 3:
        print('Congratulations, ' + name + '!')


