#!/usr/bin/env python3
import math
import random


DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def calculate_result():
    first_number = random.randint(1, 1000)
    second_number = random.randint(1, 1000)
    preliminate_number = f'{first_number} {second_number}'
    task = str(preliminate_number)
    preliminate_answer = math.gcd(first_number, second_number)
    right_answer = str(preliminate_answer)
    return task, right_answer
