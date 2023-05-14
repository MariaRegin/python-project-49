#!/usr/bin/env python3
import random


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generate_round():
    question = random.randint(2, 100)
    if is_prime(question):
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return str(question), right_answer


def is_prime(number):
    for i in range(2, int(number / 2) + 1):
        if (number % i) == 0:
            return False
    if number < 2:
        return False
    return True
