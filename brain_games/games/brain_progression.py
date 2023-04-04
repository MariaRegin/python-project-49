#!/usr/bin/env python3
import random


DESCRIPTION = 'What number is missing in the progression?'


def generate_round():
    start_num = random.randint(1, 100)
    step = random.randint(2, 5)
    length = random.randint(7, 10)
    progression = generate_progression(start_num, step, length)
    random_index = random.randint(0, len(progression) - 1)
    right_answer = str(progression[random_index])
    progression[random_index] = '..'
    task = ''
    i = 0
    while i < len(progression):
        task += str(progression[i]) + ' '
        i += 1
    return task, right_answer


def generate_progression(start_num, step, length):
    progression = [start_num]
    while length >= 0:
        progression.append(progression[-1] + step)
        length -= 1
    return progression
