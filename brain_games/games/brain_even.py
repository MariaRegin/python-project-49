#!/usr/bin/env python3

import random
import prompt


operation = random.randint(0, 1000)

def provide_task():
    return('Answer "yes" if the number is even, otherwise answer "no".')

def operation_result():
    global operation

    if operation % 2 == 0:
        return('yes')
    if operation % 2 > 0:
        return('no')
