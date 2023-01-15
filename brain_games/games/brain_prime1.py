#!/usr/bin/env python3
import random
from math import sqrt


TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def operation_result():
    number = random.randint(2, 100)
    i = 2
    while i <= sqrt(number):
        if number % i == 0:
            right_answer = 'no'
            return number, right_answer
            break
        i += 1
    else:
        right_answer = 'yes'
        return number, right_answer
