#!/usr/bin/env python3
import random


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_result():
    task = random.randint(0, 1000)
    if is_even(task):
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return task, right_answer

def is_even(question):
    if question % 2 == 0:
        return True
    return False
