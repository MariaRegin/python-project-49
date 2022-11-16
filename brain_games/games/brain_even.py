#!/usr/bin/env python3

import random
import prompt


def provide_task():
    return('Answer "yes" if the number is even, otherwise answer "no".')

def operation_type():
    operation = random.randint(0, 1000)

def operation_result():
    operation = operation_type()

    if operation % 2 == 0:
        return('yes')

    if operation % 2 > 0:
        return('no')
