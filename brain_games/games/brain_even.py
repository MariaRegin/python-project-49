#!/usr/bin/env python3
import random


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_round():
    question = random.randint(0, 1000)
    if is_even(question):
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return str(question), right_answer


def is_even(number):
    if number % 2 == 0:
        return True
    return False
