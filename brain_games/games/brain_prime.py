#!/usr/bin/env python3
import random


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generate_round():
    task = random.randint(2, 100)
    if is_prime(task):
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return task, right_answer


def is_prime(question):
    for i in range(2, int(question / 2) + 1):
        if (question % i) == 0:
            return False
    return True
