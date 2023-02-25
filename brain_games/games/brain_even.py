#!/usr/bin/env python3
import random


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def calculate_result():
    task = random.randint(0, 1000)
    if task % 2 == 0:
        right_answer = "yes"
    else:
        right_answer = 'no'
    return task, right_answer
