#!/usr/bin/env python3
import random
from math import sqrt


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def calculate_result():
    task = random.randint(2, 100)
    i = 2
    while i <= sqrt(task):
        if task % i == 0:
            right_answer = 'no'
            return task, right_answer
            break
        i += 1
    else:
        right_answer = 'yes'
        return task, right_answer
