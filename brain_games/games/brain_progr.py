#!/usr/bin/env python3
import random


TASK = 'What number is missing in the progression?'


def operation_result():
    progression = []
    element1 = random.randint(2, 8)
    element2 = random.randint(40, 50)
    step = random.randint(2, 5)
    for i in range(element1, element2, step):
        progression.append(i)
    random_index = random.randint(0, 9)
    right_answer = str(progression[random_index])
    progression[random_index] = '..'
    number = " ".join(map(str, progression[0:10]))
    return number, right_answer
