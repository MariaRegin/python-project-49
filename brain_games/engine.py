#!/usr/bin/env python3

import prompt
import random


name = prompt.string('May I have your name? ')

def welcome_user():
    print('Hello, ' + name + '!')

def explain_details():
    print(task)

def launch_game():
    tries = 0
    while tries < 3:
        operation = operation_type()
        tries += 1
        print('Question: ', operation)
        answer = prompt.string('Your answer: ')
        res = operation_result()

        if res == answer:
            print('Correct!')

        if res != answer:
            print('\"' + answer + '\"' + ' is wrong answer ;(. Correct answer was ' + res + '.' + "\nLet's try again, " + name + '!')
            break

    if tries >= 3:
        print('Congratulations, ' + name + '!')
