#!/usr/bin/env python3
import random


TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def operation_result():
    number = random.randint(0, 1000)
    if number % 2 == 0:
        right_answer = "yes"  
    else:
        right_answer = 'no'
    return number, right_answer
