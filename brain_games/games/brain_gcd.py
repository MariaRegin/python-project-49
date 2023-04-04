#!/usr/bin/env python3
import math
import random


DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def generate_round():
    first_number = random.randint(1, 100)
    second_number = random.randint(1, 100)
    task = f'{first_number} {second_number}'
    preliminate_answer = math.gcd(first_number, second_number)
    right_answer = str(preliminate_answer)
    return task, right_answer
